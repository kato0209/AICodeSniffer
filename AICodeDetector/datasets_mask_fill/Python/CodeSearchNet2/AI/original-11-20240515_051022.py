
        tables_resource = self.service.tables() \
           .get(projectId=self.project_id, datasetId=dataset_id, tableId=table_id) \
           .execute()
        return tables_resource['schema']

    def run_grant_dataset_view_access(self,
                                      source_project_dataset_table,
                                      view_dataset_table,
 