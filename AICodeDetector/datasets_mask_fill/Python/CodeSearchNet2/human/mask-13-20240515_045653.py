prefix = prefix + <extra_id_0> if prefix[-1] != delimiter else prefix prefix_split = re.split(r'(\w+[{d}])$'.format(d=delimiter), prefix, 1) previous_level = prefix_split[0] <extra_id_1> = self.list_prefixes(bucket_name, previous_level, delimiter) return False if plist is None else prefix in plist