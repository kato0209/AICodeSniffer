
        start_time = time.time()

        while True:
            response = self.get_conn().describe_operation(
                name=operation_name
            )

            if response['Status'] == 'DONE':
                if 'error' in response:
                    raise AirflowException(str(response['error']))
           