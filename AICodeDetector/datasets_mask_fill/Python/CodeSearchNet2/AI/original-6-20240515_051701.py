
    if isinstance(item, str):
        return item
    elif isinstance(item, dict):
        return _parse_config_property(item, variables)
    elif isinstance(item, list):
        return [_parse_config_property(item, variables) for item in item]
    elif isinstance(item, int):
        return _parse_config_property(item, variables)
    elif isinstance(item, float):
        return _parse_config_property(item, variables)
    elif isinstance(item, list):
        return [_parse_config_property(item, variables) for item in item]
    elif