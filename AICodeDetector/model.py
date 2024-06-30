import torch.nn as nn
from transformers import AutoTokenizer, AutoModel,AutoModelForSeq2SeqLM
import torch
from torch.nn import CrossEntropyLoss
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer, util
from pertube_data import pertubate_code
import re

from pertubate import rewrite_code

class CustomClassificationHead(nn.Module):
    def __init__(self,config, num_labels):
        super(CustomClassificationHead, self).__init__()
        self.N_MSD = 5
        self.num_labels = num_labels

        # similarity feature
        config.hidden_size = 768 + 768
        hidden_size2 = 768
        hidden_size3 = 512

        self.dense = nn.Linear(config.hidden_size, hidden_size2)
        self.dense2 = nn.Linear(hidden_size2, hidden_size3)
        self.batch_norm = nn.BatchNorm1d(hidden_size2)
        self.activation = nn.ReLU()
        self.dropouts = nn.ModuleList([nn.Dropout(0.4) for _ in range(self.N_MSD)])
        self.regressor = nn.Linear(hidden_size3, self.num_labels)
    
    def forward(self, features, **kwargs):
        # featuresの形状は [batch_size, sequence_length, hidden_size] を想定
        batch_size, hidden_size = features.size()

        # featuresを [batch_size, hidden_size] に変形
        features = features.view(batch_size, -1, hidden_size).mean(dim=1)

        # 線形変換とドロップアウトを適用
        features = self.dense(features)
        features = self.batch_norm(features)
        features = self.activation(features)
        features = self.dense2(features)

        logits = sum([self.regressor(dropout(features)) for dropout in self.dropouts]) / self.N_MSD
        return logits

class CustomBertModel(nn.Module):
    def __init__(self, loss_ratio=0.5, sub_loss_ratio=0.5, alpha=0.5, beta=0.8):
        super(CustomBertModel, self).__init__()
        self.model = AutoModel.from_pretrained("microsoft/codebert-base")
        self.sentence_model = SentenceTransformer('Sakil/sentence_similarity_semantic_search')
        self.dropout = nn.Dropout(self.model.config.hidden_dropout_prob)
        self.classifier = CustomClassificationHead(self.model.config, num_labels=2)
        #self.id_classifier = CustomClassificationHead(self.model.config, num_labels=7)
        self.num_labels = 2
        self.num_id_labels = 7
        #self.alpha = 0.1
        self.loss_ratio = loss_ratio
        self.alpha = alpha
        self.beta = beta
        self.sub_loss_ratio = sub_loss_ratio
        
    
    def return_model(self):
        return self.model
    
    def forward(self, input_ids=None, attention_mask=None, labels=None, original_code=None, perturb_code=None):
        
        sentences = []
        for code in original_code:
            sentences.append(code)
        for code in perturb_code:
            sentences.append(code)
        embedings = self.sentence_model.encode(sentences)
        cos_sim = util.cos_sim(embedings, embedings)
        similarity_scores = [cos_sim[i, len(original_code) + i] for i in range(len(original_code))]
        similarity_scores = torch.tensor(similarity_scores).view(-1, 1).to(input_ids.device)
        #similarity_scoresを[size, 1]から[size, 768]に変換
        similarity_scores = similarity_scores.repeat(1, 768)

        outputs = self.model(input_ids, attention_mask=attention_mask)
        pooled_output = pooled = outputs[1]
        pooled_output = self.dropout(pooled_output)
        new_pooled_output = torch.cat([pooled_output, similarity_scores], dim=-1)

        loss = None
        cos_loss = None
        if labels is not None:
            dist = ((new_pooled_output.unsqueeze(1) - new_pooled_output.unsqueeze(0)) ** 2).mean(-1)
            mask = (labels.unsqueeze(1) == labels.unsqueeze(0)).float()
            mask = mask - torch.diag(torch.diag(mask))
            neg_mask = (labels.unsqueeze(1) != labels.unsqueeze(0)).float()
            max_dist = (dist * mask).max()
            cos_loss = (dist * mask).sum(-1) / (mask.sum(-1) + 1e-3) + (F.relu(max_dist - dist) * neg_mask).sum(-1) / (neg_mask.sum(-1) + 1e-3)
            cos_loss = cos_loss.mean()

            loss_fct = CrossEntropyLoss()

            logits = self.classifier(new_pooled_output)
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
            loss = self.loss_ratio * loss + self.alpha * cos_loss
        else:
            logits = self.classifier(new_pooled_output)

        output = (logits,) + outputs[2:]
        output = output + (pooled,)
        return ((loss, cos_loss) + output) if loss is not None else output


class CustomCodeLlamaModel(nn.Module):
    def __init__(self, model, tokenizer, sentence_model, sentence_model_tokenizer):
        super(CustomCodeLlamaModel, self).__init__()
        self.model = model
        self.tokenizer = tokenizer
        self.sentence_model = sentence_model
        self.sentence_model_tokenizer = sentence_model_tokenizer
    
    def rewrite_code(self, codes, model_config, args):
        prompt = """
        Generate the following Python code rewrite according to your idea.
        Please do not output anything other than the rewritten Python code.
        ```
        {code}
        ```
        """

        tokenizer = model_config['tokenizer']
        model = model_config['model']

        # [batch_size, token_length]の配列を用意
        y = [[0 for _ in range(args.token_length)] for _ in range(args.batch_size)]
        state = [[0 for _ in range(args.token_length)] for _ in range(args.batch_size)]
        

        rewrite_codes = []
        i = 0
        for code in codes:
            input_prompt = prompt.format(code=code)
            input_ids = tokenizer(input_prompt, return_tensors="pt", truncation=True, max_length=128).input_ids
            input_ids = input_ids.to(args.DEVICE)
            
            # トークンごとの生成を開始
            output_ids = input_ids
            j = 0
            for _ in range(128):  # 生成を128トークンに制限
                outputs = model.generate(output_ids, do_sample=True, max_length=output_ids.size(-1) + 1, 
                                        top_p=0.95, temperature=0.1, pad_token_id=tokenizer.pad_token_id, use_cache=True)
                y[i][j] = outputs[:, -1].unsqueeze(-1)
                state[i][j] = output_ids
                if outputs[:, -1].unsqueeze(-1) == 0:
                    output_ids = torch.cat([output_ids, outputs[:, -1].unsqueeze(-1)], dim=-1)
                if output_ids[0, -1] == tokenizer.eos_token_id:
                    break
                j += 1
            output_sentence = tokenizer.decode(torch.cat(y[i], dim=-1)[0], skip_special_tokens=True)
            rewrite_codes.append(output_sentence)
            i += 1
        
        return rewrite_codes, y, state

    def forward(self, original_codes=None, labels=None, args=None, model_config=None):
        #_, perturbed_codes = pertubate_code(original_codes, model_config, args)
        perturbed_codes, y, state = self.rewrite_code(original_codes, model_config, args)

        similarity_scores = self._calc_similarity(original_codes, perturbed_codes, args, model_config)

        ai_similarity = []
        human_similarity = []
        for i in range(len(similarity_scores)):
            if labels[i] == 1:
                ai_similarity.append(similarity_scores[i])
            else:
                human_similarity.append(similarity_scores[i])
        ai_similarity = torch.tensor(ai_similarity, requires_grad=True).view(-1, 1).to(self.model.device)
        human_similarity = torch.tensor(human_similarity, requires_grad=True).view(-1, 1).to(self.model.device)

        #similarity_scoresの平均をベースラインに
        loss = 0.0
        for n in range(args.batch_size):
            token_length = len(y[n])
            for t in range(token_length):
                if y[n][t] == 0:
                    continue
                outputs = self.model(input_ids=state[n][t])
                logits = outputs.logits

                # 入力シーケンスの最後のトークンに対するロジットを抽出
                last_token_logits = logits[0, -1, :]
                # ログ確率を計算
                log_probs = F.log_softmax(last_token_logits, dim=-1)
                target_token_log_prob = log_probs[y[n][t].item()]

                if labels[n] == 1:
                    baseline = torch.mean(ai_similarity)
                    reward = similarity_scores[n].item()
                    R = reward - baseline
                else:
                    baseline = 1 - torch.mean(human_similarity)
                    reward = 1 - similarity_scores[n].item()
                    R = (reward - baseline) * 0.5
                loss += -target_token_log_prob * R
        loss /= args.batch_size * token_length

        return loss, similarity_scores
    
    def _calc_similarity(self, original_codes, perturbed_codes, args=None, model_config=None):
        similarity_scores = []
        for i in range(len(original_codes)):
            encoded_inputs = self.sentence_model_tokenizer(original_codes[i], return_tensors="pt", truncation=True, max_length=128).to(self.model.device)
            with torch.no_grad():
                outputs = self.sentence_model(input_ids=encoded_inputs.input_ids)
            embeddings1 = outputs.last_hidden_state.mean(dim=1)

            encoded_inputs = self.sentence_model_tokenizer(perturbed_codes[i], return_tensors="pt", truncation=True, max_length=128).to(self.model.device)
            with torch.no_grad():
                outputs = self.sentence_model(input_ids=encoded_inputs.input_ids)
            embeddings2 = outputs.last_hidden_state.mean(dim=1)

            cos_sim = util.cos_sim(embeddings1, embeddings2)
            similarity_scores.append(cos_sim.item())
        similarity_scores = torch.tensor(similarity_scores).view(-1, 1).to(self.model.device)
        return similarity_scores
    
    def _calc_similarity_cutom(self, original_codes, perturbed_codes, args=None, model_config=None):
        input_ids = []
        attention_mask = []
        for i in range(len(original_codes)):
            encoded_inputs = self.sentence_model_tokenizer(original_codes[i], return_tensors="pt", truncation=True, max_length=128).to(self.model.device)
            input_ids.append(encoded_inputs.input_ids)
            attention_mask.append(encoded_inputs.attention_mask)
        
        input_ids_p = []
        attention_mask_p = []
        for i in range(len(perturbed_codes)):
            encoded_inputs = self.sentence_model_tokenizer(perturbed_codes[i], return_tensors="pt", truncation=True, max_length=128).to(self.model.device)
            input_ids_p.append(encoded_inputs.input_ids)
            attention_mask_p.append(encoded_inputs.attention_mask)
        
        similarity_scores = []
        with torch.no_grad():
            embeddings1 = self.sentence_model.output_embeddings(input_ids, attention_mask)
            embeddings2 = self.sentence_model.output_embeddings(input_ids_p, attention_mask_p)
        cos_sim = util.cos_sim(embeddings1, embeddings2)
        for i in range(len(original_codes)):
            similarity_scores.append(cos_sim[i, i].item())
        similarity_scores = torch.tensor(similarity_scores).view(-1, 1).to(self.model.device)
        return similarity_scores
    
    def calc_similarity(self, original_codes, args=None, model_config=None):
        perturbed_codes, _, _ = self.rewrite_code(original_codes, model_config, args)
        
        similarity_scores = []
        for i in range(len(original_codes)):
            encoded_inputs = self.sentence_model_tokenizer(original_codes[i], return_tensors="pt", truncation=True, max_length=128).to(self.model.device)
            with torch.no_grad():
                outputs = self.sentence_model(input_ids=encoded_inputs.input_ids)
            embeddings1 = outputs.last_hidden_state.mean(dim=1)

            encoded_inputs = self.sentence_model_tokenizer(perturbed_codes[i], return_tensors="pt", truncation=True, max_length=128).to(self.model.device)
            with torch.no_grad():
                outputs = self.sentence_model(input_ids=encoded_inputs.input_ids)
            embeddings2 = outputs.last_hidden_state.mean(dim=1)

            cos_sim = util.cos_sim(embeddings1, embeddings2)
            similarity_scores.append(cos_sim.item())
        similarity_scores = torch.tensor(similarity_scores).view(-1, 1).to(self.model.device)
        return similarity_scores

    def calc_similarity_custom(self, original_codes, args=None, model_config=None):
        perturbed_codes, _, _ = self.rewrite_code(original_codes, model_config, args)
        input_ids = []
        attention_mask = []
        for i in range(len(original_codes)):
            encoded_inputs = self.sentence_model_tokenizer(original_codes[i], return_tensors="pt", padding="max_length", truncation=True, max_length=128).to(self.model.device)
            input_ids.append(encoded_inputs.input_ids)
            attention_mask.append(encoded_inputs.attention_mask)
        # input_idsをtensorに変換
        input_ids = torch.cat(input_ids, dim=0)
        attention_mask = torch.cat(attention_mask, dim=0)
        
        input_ids_p = []
        attention_mask_p = []
        for i in range(len(perturbed_codes)):
            encoded_inputs = self.sentence_model_tokenizer(perturbed_codes[i], return_tensors="pt", padding="max_length", truncation=True, max_length=128).to(self.model.device)
            input_ids_p.append(encoded_inputs.input_ids)
            attention_mask_p.append(encoded_inputs.attention_mask)
        # input_ids_pをtensorに変換
        input_ids_p = torch.cat(input_ids_p, dim=0)
        attention_mask_p = torch.cat(attention_mask_p, dim=0)
        
        with torch.no_grad():
            embeddings1 = self.sentence_model.output_embeddings(input_ids, attention_mask)
            embeddings2 = self.sentence_model.output_embeddings(input_ids_p, attention_mask_p)
        cos_sim = self.sentence_model.sim(embeddings1, embeddings2)
        return cos_sim

class MLPLayer(nn.Module):
    """
    Head for getting sentence representations over RoBERTa/BERT's CLS representation.
    """

    def __init__(self, config):
        super().__init__()
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        self.activation = nn.Tanh()

    def forward(self, features, **kwargs):
        x = self.dense(features)
        x = self.activation(x)

        return x

class Similarity(nn.Module):
    """
    Dot product or cosine similarity
    """

    def __init__(self):
        super().__init__()
        self.temp = 0.05
        self.cos = nn.CosineSimilarity(dim=-1)

    def forward(self, x, y):
        return self.cos(x, y) / self.temp


class Pooler(nn.Module):
    """
    Parameter-free poolers to get the sentence embedding
    'cls': [CLS] representation with BERT/RoBERTa's MLP pooler.
    'cls_before_pooler': [CLS] representation without the original MLP pooler.
    'avg': average of the last layers' hidden states at each token.
    'avg_top2': average of the last two layers.
    'avg_first_last': average of the first and the last layers.
    """
    def __init__(self):
        super().__init__()
        self.pooler_type = 'cls'

    def forward(self, attention_mask, outputs):
        last_hidden = outputs.last_hidden_state
        pooler_output = outputs.pooler_output
        hidden_states = outputs.hidden_states

        if self.pooler_type in ['cls_before_pooler', 'cls']:
            return last_hidden[:, 0]
        elif self.pooler_type == "avg":
            return ((last_hidden * attention_mask.unsqueeze(-1)).sum(1) / attention_mask.sum(-1).unsqueeze(-1))
        elif self.pooler_type == "avg_first_last":
            first_hidden = hidden_states[1]
            last_hidden = hidden_states[-1]
            pooled_result = ((first_hidden + last_hidden) / 2.0 * attention_mask.unsqueeze(-1)).sum(1) / attention_mask.sum(-1).unsqueeze(-1)
            return pooled_result
        elif self.pooler_type == "avg_top2":
            second_last_hidden = hidden_states[-2]
            last_hidden = hidden_states[-1]
            pooled_result = ((last_hidden + second_last_hidden) / 2.0 * attention_mask.unsqueeze(-1)).sum(1) / attention_mask.sum(-1).unsqueeze(-1)
            return pooled_result
        else:
            raise NotImplementedError

class SimilarityModel(nn.Module):
    def __init__(self, model_config):
        super(SimilarityModel, self).__init__()
        self.model = model_config['model']
        self.tokenizer = model_config['tokenizer']
        self.pooler = Pooler()
        self.MLP = MLPLayer(self.model.config)
        self.sim = Similarity()
    
    def forward(self, input_ids, attention_mask):
        batch_size = input_ids.size(0)
        num_sent = input_ids.size(1)
        input_ids = input_ids.view((-1, input_ids.size(-1)))
        attention_mask = attention_mask.view((-1, attention_mask.size(-1)))

        outputs = self.model(input_ids, attention_mask=attention_mask)
        pooled_output = self.pooler(attention_mask, outputs)
        pooled_output = self.MLP(pooled_output)
        pooler_output = pooled_output.view((batch_size, num_sent, pooled_output.size(-1)))
        z1 = pooler_output[:,0]

        outputs2 = self.model(input_ids, attention_mask=attention_mask)
        pooled_output2 = self.pooler(attention_mask, outputs2)
        pooled_output2 = self.MLP(pooled_output2)
        pooler_output2 = pooled_output2.view((batch_size, num_sent, pooled_output2.size(-1)))
        z2 = pooler_output2[:,0]
        cos_sim = self.sim(z1.unsqueeze(1), z2.unsqueeze(0))
        labels = torch.arange(cos_sim.size(0)).long().to(self.model.device)
        loss_fct = nn.CrossEntropyLoss()
        loss = loss_fct(cos_sim, labels)
        return (loss, cos_sim)
    def output_embeddings(self, input_ids, attention_mask):
        batch_size = input_ids.size(0)
        input_ids = input_ids.view((-1, input_ids.size(-1)))
        attention_mask = attention_mask.view((-1, attention_mask.size(-1)))

        outputs = self.model(input_ids, attention_mask=attention_mask)
        pooled_output = self.pooler(attention_mask, outputs)
        pooled_output = self.MLP(pooled_output)
        pooler_output = pooled_output.view((batch_size, pooled_output.size(-1)))

        return pooler_output
