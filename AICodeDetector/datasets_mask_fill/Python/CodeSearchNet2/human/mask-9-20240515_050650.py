if file_path is None or file_path == '-': if sys.stdin.isatty(): raise RuntimeError('To <extra_id_0> <extra_id_1> from terminal please use <extra_id_2> mode') f = sys.stdin else: f = open(file_path, encoding='utf8') model: Chainer = build_model(config) args_count = len(model.in_x) while True: batch = list((l.strip() for l in islice(f, batch_size * args_count))) if not batch: break