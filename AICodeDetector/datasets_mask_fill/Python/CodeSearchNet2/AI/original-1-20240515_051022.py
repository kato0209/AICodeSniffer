
        client = self.get_conn()
        product_set_id = ProductSetId(product_set_id)
        product_set = ProductSet(
            location=location,
            product_set_id=product_set_id,
            project_id=project_id,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )
        return client.add_product_to_product_set(
        