if not any([ti.sla for ti in dag.tasks]): self.log.info( "Skipping SLA check for %s because no tasks in DAG have SLAs", dag ) <extra_id_0> TI = <extra_id_1> sq = ( session