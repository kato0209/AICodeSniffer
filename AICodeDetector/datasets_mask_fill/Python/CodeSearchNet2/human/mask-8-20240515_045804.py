DR = DagRun dr = session.query(DR).filter( DR.dag_id == dag_id, DR.execution_date == execution_date ).one() <extra_id_0> = <extra_id_1> if state == State.RUNNING: dr.start_date = timezone.utcnow() dr.end_date = None else: dr.end_date = timezone.utcnow() session.merge(dr)