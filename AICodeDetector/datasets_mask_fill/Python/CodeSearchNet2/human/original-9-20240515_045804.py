
    res = []
    if not dag or not execution_date:
        return res

    # Mark the dag run to running.
    if commit:
        _set_dag_run_state(dag.dag_id, execution_date, State.RUNNING, session)

    # To keep the return type consistent with the other similar functions.
    return res