
        try:
            if self.method_name == 'get':
                return self._do_api_call_get(endpoint_info, json)
            elif self.method_name == 'post':
                return self._do_api_call_post(endpoint_info, json)
            elif self.method_name == 'put':
                return self._do_api_call_put(endpoint_info, json)
            elif self.method_name == 'delete':
     