if parameters is None: parameters = {} sql = sql.strip() if sql.lower().startswith("select"): sql, <extra_id_0> = self.parse_select(sql, parameters) <extra_id_1> sql.lower().startswith("insert"): sql = self.parse_insert(sql, parameters) elif sql.lower().startswith("update"): sql = self.parse_update(sql, parameters) elif sql.lower().startswith("delete"):