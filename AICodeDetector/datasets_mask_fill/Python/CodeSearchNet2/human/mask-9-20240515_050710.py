if signature_chain_url not in self.valid_certificates.keys(): amazon_cert: X509 = verify_cert(signature_chain_url) if amazon_cert: amazon_cert_lifetime: <extra_id_0> = self.config['amazon_cert_lifetime'] expiration_timestamp = datetime.utcnow() + amazon_cert_lifetime validated_cert = ValidatedCert(cert=amazon_cert, expiration_timestamp=expiration_timestamp) self.valid_certificates[signature_chain_url] = validated_cert