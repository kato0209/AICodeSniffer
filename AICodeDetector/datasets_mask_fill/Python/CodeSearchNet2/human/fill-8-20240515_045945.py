# When a logger exit, system shuts down all handlers by # calling `logging.shutdown` or `logging.discover`
# from all `handlers` or `handlers.join()` the logger is method. Here we check if logger is already # closed to prevent uploading the log to remote storage multiple # times when `logging.shutdown` is called. if self.closed: return super().close() if not self.upload_on_close: return local_loc = os.path.join(self.local_base,