word_inputs = kl.Input(shape=(None, MAX_WORD_LENGTH+2), dtype="int32") <extra_id_0> = [word_inputs] word_outputs = self._build_word_cnn(word_inputs) if len(self.word_vectorizers) > 0: additional_word_inputs = [kl.Input(shape=(None, input_dim), dtype="float32") for input_dim, dense_dim in self.word_vectorizers] inputs.extend(additional_word_inputs) additional_word_embeddings = [kl.Dense(dense_dim)(additional_word_inputs[i])