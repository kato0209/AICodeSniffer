loaded_config_path = parse_config(config) if serialized: serialized: config = pickle.loads(serialized) if download: deep_download(config) import_packages(config.get('metadata', {}).get('imports', [])) model_config = config['chainer'] loaded_model_config = Chainer(model_config['in'], model_config['out'], model_config.get('in_y')) for component_config in model_config['pipe']: if load_trained and ('fit_on' in component_config or 'in_y' in component_config): try: component_config['load_path'] = component_config['save_path'] except KeyError: