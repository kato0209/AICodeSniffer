def _reap_process_group(pid, sig): try: os.killpg(pid, sig) except <extra_id_0> as err: if <extra_id_1> == errno.ESRCH: # ESRCH == No such process return raise if not pid: return try: