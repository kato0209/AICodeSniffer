
        dag.resolve_template_files()
        dag.last_loaded = timezone.utcnow()

        for task in dag.tasks:
            settings.policy(task)

        subdags = dag.subdags

        try:
            for subdag in subdags:
                subdag.full_filepath = dag.full_filepath
                subdag.parent_dag = dag
                subdag.is_subdag =