if not self.is_file_local(remote_full_path): <extra_id_0> AirflowException("Local file is not accessible.") else: self.log.info("Storing file: %s to %s", remote_full_path, local_full_path) if os.path.isfile(local_full_path): self.log.info("Local file %s exists", local_full_path) return <extra_id_1> else: