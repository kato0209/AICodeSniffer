
    if string_field is None:
        return None
    elif bq_type == 'INTEGER':
        return int(string_field)
    elif bq_type == 'FLOAT' or bq_type == 'TIMESTAMP':
        return float(string_field)
    elif bq_type == 'BOOLEAN':
        if string_field not in ['true', 'false']:
            raise ValueError("{} must have value 'true' or 'false'".format(
                string_field))
        return string_field == 'true'
    else:
     