
        self.log.info('Creating a new ACL entry in bucket: %s', bucket_name)
        client = self.get_conn()
        bucket = client.bucket(bucket_name=bucket_name)
        bucket.acl.reload()
        bucket.acl.entity_from_dict(entity_dict={"entity": entity, "role": role})
        if user_project:
            bucket.acl.user_project = user_project
        bucket.acl.save()

        self.log.info('A new ACL entry created in bucket: %s', bucket_name)