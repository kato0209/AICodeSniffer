if isinstance(item, str): <extra_id_0> item <extra_id_1> isinstance(item, dict): return _parse_config_property(item, variables) <extra_id_2> isinstance(item, list): return [_parse_config_property(item, variables) for item in item] elif isinstance(item, int): return _parse_config_property(item, variables) elif isinstance(item, float): return _parse_config_property(item, variables) elif isinstance(item, list): return [_parse_config_property(item, variables) for item in item] elif