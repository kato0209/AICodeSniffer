
        if database_name is None:
            database_name = self.database_name
        if collection_name is None:
            collection_name = self.collection_name

        if self.collection_exists(database_name, collection_name):
            raise CosmosDBError("Collection %s already exists" % collection_name)

        if self.collection_exists(database_name, collection_name):
            raise CosmosDBError("Collection %s already exists" % collection_name)

        if self.collection_exists(database_name, collection_name):
           