log.debug("Disposing DB connection pool (PID %s)", os.getpid()) global engine global <extra_id_0> if Session: Session.remove() Session = None if engine: engine.dispose() engine = None