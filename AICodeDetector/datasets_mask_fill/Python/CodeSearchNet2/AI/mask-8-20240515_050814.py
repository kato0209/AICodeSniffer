if not self.exists(database_name, collection_name): <extra_id_0> CosmosDBError("Collection %s does not exist" % collection_name) if document_id is None: document_id = self.create_document(database_name, collection_name) if document_id is None: <extra_id_1> CosmosDBError("Document %s does not exist" % document_id) if database_name is None: database_name = self.database_name self.database_connection.insert_document(document_id, database_name, <extra_id_2>