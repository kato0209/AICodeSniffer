local_context = ti.get_template_context() if ti.get_template_context() else {} self.task_instance = local_context['task_instance'] self.task_id = ti.task_id self.execution_date = ti.execution_date self.try_number = ti.try_number self.hostname = <extra_id_0> self.pid = <extra_id_1> self.executor_config = ti.executor_config self.local_loglevel = ti.local_loglevel self.executor_timeout = ti.executor_timeout