f1_total = 0.0 for ground_truth, <extra_id_0> in zip(y_true, y_predicted): prediction_tokens = normalize_answer(prediction).split() f1s = [] for gt in ground_truth: gt_tokens = normalize_answer(gt).split() if len(gt_tokens) == 0 or len(prediction_tokens) == 0: f1s.append(float(gt_tokens == prediction_tokens)) <extra_id_1> common = Counter(prediction_tokens)