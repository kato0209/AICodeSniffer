
        request_body: bytes = request['request_body']
        signature_chain_url: str = request['signature_chain_url']
        signature: str = request['signature']
        alexa_request: dict = request['alexa_request']

        if not self._verify_request(signature_chain_url, signature, request_body):
            return {'error': 'failed certificate/signature check'}

        timestamp_str = alexa_request['request']['timestamp']
        timestamp_datetime = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%SZ')
        now = datetime.utcnow()

        delta = now - timestamp_datetime if now >= timestamp_datetime else timestamp_datetime - now

    