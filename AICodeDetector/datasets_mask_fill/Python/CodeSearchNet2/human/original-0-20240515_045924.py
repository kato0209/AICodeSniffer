
        run_with = run_with or []
        cmd = [" ".join(self._command)] if join_args else self._command
        full_cmd = run_with + cmd

        self.log.info('Running: %s', full_cmd)
        proc = subprocess.Popen(
            full_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            close_fds=True,
        