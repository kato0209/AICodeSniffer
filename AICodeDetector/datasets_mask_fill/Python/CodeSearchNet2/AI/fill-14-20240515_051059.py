TI = TaskInstance ti_concurrency_query = ( TI .query(TI.task_id, TI.dag_id, func.count('*')) .filter(TI.state.in_(states)) .group_by(TI.task_id, TI.dag_id) ) task_map = defaultdict(set) for result in ti_concurrency_query: task_id, dag_id, states = = result task_map[(dag_id, task_id)] =