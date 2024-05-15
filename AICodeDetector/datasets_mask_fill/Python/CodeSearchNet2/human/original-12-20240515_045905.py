

        if not dataset_id or not isinstance(dataset_id, str):
            raise ValueError("dataset_id argument must be provided and has "
                             "a type 'str'. You provided: {}".format(dataset_id))

        dataset_project_id = project_id if project_id else self.project_id

        try:
            dataset_resource = self.service.datasets().get(
                datasetId=dataset_id, projectId=dataset_project_id).execute(num_retries=self.num_retries)
      