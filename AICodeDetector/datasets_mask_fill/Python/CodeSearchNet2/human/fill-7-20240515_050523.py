news_dir = download_news20(source_dir) sample_path = [] # list of path to samples label_id = 0 for name in sorted(os.listdir(news_dir)): path = os.path.join(news_dir, name) label_id += 1 if os.path.isdir(path): for fname in sorted(os.listdir(path)): if fname.isdigit(): fpath = os.path.join(path, fname)