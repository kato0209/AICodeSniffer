
        if dag_id in self.dags:
            dag = self.dags[dag_id]
            if dag.has_task(dag_id):
                return dag
            else:
                raise AirflowException(
                    'dag_id could not be found: {}. Either the DAG '
              