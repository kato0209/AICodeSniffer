
        if not project_id:
            raise ValueError("Project ID should be set")
        instance = instance.strip()
        project_id = project_id.strip()
        self.log.info("Deleting database: %s", database)
        try:
            instance = self.get_conn().instances().delete(
                project=project_id,
                instance=instance,
               