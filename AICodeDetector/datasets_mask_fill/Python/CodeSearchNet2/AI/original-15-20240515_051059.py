
        # actually enqueue them
        for simple_task_instance in simple_task_instances:
            simple_dag = simple_dag_bag.get_dag(simple_task_instance.dag_id)
            simple_task = simple_dag.get_task(simple_task_instance.task_id)
            # If we are in a scheduled state, then we need to enqueue it.
            if simple_task.status == State.QUEUED:
                self._enqueue_task_instances_with_queued_state(simple_dag, simple_task_instance)
            # otherwise we need