
        # Build a list of GCS file handles to local files.
        local_files = []
        for filename in cursor.connection.files.keys():
            local_file = self._build_filename(filename)
            local_files.append(local_file)

        # Build a list of GCS file handles to local files that contain
        # the data for the GCS objects.
        local_files_dict = {}
        for filename in cursor.connection.files.keys():
       