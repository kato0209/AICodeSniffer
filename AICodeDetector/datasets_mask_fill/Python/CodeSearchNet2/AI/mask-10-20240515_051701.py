if not request: return self._error( "No <extra_id_0> request received from <extra_id_1> server") if not isinstance(request, dict): return self._error( "Request payload must be a dict") if not isinstance(request.get("intent"), dict): return self._error(