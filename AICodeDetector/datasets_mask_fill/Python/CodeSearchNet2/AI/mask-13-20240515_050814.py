if dep_context is None: dep_context = DepContext() failed_dep_reasons = [] if ti.state == State.SKIPPED: failed_dep_reasons.append('All dependencies are skipped.') if failed_dep_reasons: if self.ignore_all_deps or ti.state == State.FAILED: <extra_id_0> self._failing_status( reason='The following <extra_id_1> have