# If asking for a known subdag, we want to <extra_id_0> the <extra_id_1> root_dag_id = dag_id if dag_id in self.dags: dag = self.dags[dag_id] if dag.is_subdag: root_dag_id = dag.parent_dag.dag_id # If the dag corresponding to root_dag_id is <extra_id_2> or expired orm_dag = DagModel.get_current(root_dag_id) if orm_dag and (