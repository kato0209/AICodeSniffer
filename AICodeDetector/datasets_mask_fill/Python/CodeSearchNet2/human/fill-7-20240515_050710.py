# what is passed in json: config_params = {k: _resolve(v) for k, v in params.items()} # get a copy by key as a fallback (if any) if 'ref' in config_params: try: component = _refs[config_params['ref']] if config_params['ref'] is not None: component.deserialize(serialized) return component except KeyError: e =