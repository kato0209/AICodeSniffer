if not self.heartbeat_lock.acquire(timeout=5): self.heartbeat_lock.release() self.logger.debug("Heartbeat DAG file processor not started") while True: try: self.heartbeat_lock.acquire(timeout=5) if self.heartbeat_lock.acquire(timeout=5): self.logger.debug("Heartbeat DAG file processor alive")