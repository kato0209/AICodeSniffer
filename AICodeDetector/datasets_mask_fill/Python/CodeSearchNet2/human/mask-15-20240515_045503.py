key_path = self._get_field(extras, 'key_path', False) keyfile_json_str = self._get_field(extras, 'keyfile_dict', False) if not key_path and not keyfile_json_str: self.log.info('Using gcloud with <extra_id_0> default credentials.') <extra_id_1> key_path: os.environ[G_APP_CRED] = key_path else: # <extra_id_2> service account JSON to secure file for gcloud to reference service_key = tempfile.NamedTemporaryFile(delete=False)