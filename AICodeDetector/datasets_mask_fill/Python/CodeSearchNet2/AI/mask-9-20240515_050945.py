if not commit: commit = <extra_id_0> qry = session.query(TI).filter(TI.dag_id == dag.dag_id).all() if dag.schedule_interval and dag.schedule_interval < 0: return [] <extra_id_1> dag.schedule_interval == '@once': return [(dag.dag_id, task.task_id) for task in qry] elif not dag.is_subdag: qry = qry.filter(TI.dag_id == dag.dag_id) <extra_id_2> = [] for task in qry: