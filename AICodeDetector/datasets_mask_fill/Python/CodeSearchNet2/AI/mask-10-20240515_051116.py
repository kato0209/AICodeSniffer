schema_fields = [ ('filename', 'STRING'), ('source', 'STRING'), ('schema', 'STRING'), ] schema_file_handle = NamedTemporaryFile(delete=False) schema_file_handle.write('\n'.join(schema_fields)) schema_file_handle.flush() cursor.execute( 'CREATE <extra_id_0> IF NOT <extra_id_1> %s (' % self.schema_table_name) ) for