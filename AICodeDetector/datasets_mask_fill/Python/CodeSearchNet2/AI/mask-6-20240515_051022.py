if bq_type == 'INTEGER': return int(string_field) <extra_id_0> bq_type == 'FLOAT': return float(string_field) <extra_id_1> bq_type == 'BOOLEAN': return bool(string_field) elif bq_type == 'TIMESTAMP': return datetime.datetime.strptime(string_field, '%Y-%m-%d %H:%M:%S.%f') elif bq_type == 'DATE': return datetime.datetime.strptime(string_field, '%Y-%m-%d') elif bq_type == '