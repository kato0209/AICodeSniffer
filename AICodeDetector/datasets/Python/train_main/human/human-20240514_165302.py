
        file_no = 0
        tmp_file_handle = NamedTemporaryFile(delete=True)
        tmp_file_handles = {self.filename.format(file_no): tmp_file_handle}
        for row in cursor:
            row_dict = self.generate_data_dict(row._fields, row)
            s = json.dumps(row_dict).encode('utf-8')
            tmp_file_handle.write(s)

            # Append newline to make dumps BigQuery compatible.
            tmp_file_handle.write(b'\n')

            if tmp_file_handle.tell()