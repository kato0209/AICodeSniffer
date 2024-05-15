
        if not bucket_name:
            (bucket_name, wildcard_key) = self.parse_s3_url(wildcard_key)
        prefix = re.split(r'\*', prefix)[-1]
        delimiter = re.split(r'\s*,\s*', delimiter)[-1]
        prefix_len = len(prefix)
        delimiter_len = len(delimiter)
        if prefix_len!= delimiter_len:
            raise ValueError('Prefix length (%d) must be equal to delimiter '
                             '(%d)'