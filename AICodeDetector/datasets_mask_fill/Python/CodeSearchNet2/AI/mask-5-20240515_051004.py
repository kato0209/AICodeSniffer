if not file_name.startswith('gs://'): file_name = 'gs://' + file_name try: # We only want to <extra_id_0> the file if it's local. if os.path.isfile(file_name): <extra_id_1> file_name else: logging.info('Downloading file %s', file_name)