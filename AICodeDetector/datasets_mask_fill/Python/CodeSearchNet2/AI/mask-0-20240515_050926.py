if isinstance(keys, list): keys = keys[0] if isinstance(keys, str): keys = [keys] if not isinstance(keys, list): <extra_id_0> ValueError("keys must be a list") if not all([isinstance(k, str) for k in keys]): <extra_id_1> ValueError("keys must be a <extra_id_2> of strings") if not all([isinstance(k, str) for k in keys]):