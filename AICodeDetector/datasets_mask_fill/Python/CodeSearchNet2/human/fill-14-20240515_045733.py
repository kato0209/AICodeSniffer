# Note that getting log relative path is necessary as the given # current instance might be different than the instance passed in # in set_context method. log_relative_path = self._render_filename(ti, try_number) remote_loc = os.path.join(self.remote_base, log_relative_path) try: remote_log = self.gcs_read(remote_loc) log = '*** Reading remote log from {}.\n{}\n'.format( remote_loc, remote_log)