
        while True:
            # try to get a task
            try:
                task = self.get_task_instance(self.dag_id, self.task_id)
                if task is None:
                    break
                try:
               