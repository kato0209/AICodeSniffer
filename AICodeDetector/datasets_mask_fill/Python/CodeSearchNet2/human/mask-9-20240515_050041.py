from six.moves <extra_id_0> urllib root = os.path.expanduser(root) if not filename: filename = os.path.basename(url) fpath = os.path.join(root, filename) makedir_exist_ok(root) # downloads file if os.path.isfile(fpath) and check_integrity(fpath, md5): print('Using downloaded and <extra_id_1> file: ' + fpath) else: try: print('Downloading ' + <extra_id_2> + ' to ' + fpath) urllib.request.urlretrieve(