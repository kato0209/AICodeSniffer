return task_instance.status == RUNNING and run(self): self.log.info("Starting the executor") # Get the locks executor = Synchronizer(self._config) self.executor_info = executor.get_executor_info() self.executor_info.start() self.log.info("Executor started") try: self.log.info("Starting the scheduler") self.scheduler_info = self.executor_info.get_scheduler_info() self.scheduler_info.start()