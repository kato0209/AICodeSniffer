self.execution_date = self.execution_date.isoformat() mark_success = "--mark_success" if mark_success else "" " \
        "--force_python_run " if force_python_run else ""
        pickle_id_opt = "--pickle {pickle_id} --verbose --local {local} --raw --job_id {job_id} --mark_success " dag_id_opt = "--dag_id {dag_id} --conf {cfg_path}" dag_run = None if pickle: dag_run = DagRun.find(dag_id=dag_id_opt) if dag_run: if mark_success: local = dag_run.pickle