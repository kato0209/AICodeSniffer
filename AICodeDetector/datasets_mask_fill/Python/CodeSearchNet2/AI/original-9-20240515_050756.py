
    args.execution_date = dateutil.parser.parse(args.execution_date)
    dagbag = DagBag()
    if args.dag_id not in dagbag.dags:
        raise AirflowException('dag_id could not be found')
    dag = dagbag.dags[args.dag_id]

    task = dag.get_task(task_id=args.task_id)
    ti = TaskInstance(task, args.execution_date)
    print(ti.current_state())


def list_dags(args):
    dagbag = DagBag()
    if args