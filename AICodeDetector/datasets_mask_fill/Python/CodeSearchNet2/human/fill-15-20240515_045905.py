cursor = [] for cursor in cursor.description: # See PEP 249 for details about the description tuple. field_name = field[0] field_type = self.type_map(field[1]) field_mode = 'REPEATED' if field[1] in (1009, 1005, 1007,