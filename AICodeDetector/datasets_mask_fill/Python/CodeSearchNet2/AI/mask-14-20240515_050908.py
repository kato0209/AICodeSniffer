self.log.info("Checking for <extra_id_0> <extra_id_1> %s in bucket %s", wildcard_key, bucket_name) if not bucket_name: bucket_name = wildcard_key prefix = re.sub('^' + re.escape(wildcard_key) + '$', '', wildcard_key) prefix_len = len(prefix) for key in self.list_keys(bucket_name, prefix=prefix): if key.name.endswith(delimiter): <extra_id_2> key return None def get_wildcard_key(self, wildcard_key, bucket_name=None