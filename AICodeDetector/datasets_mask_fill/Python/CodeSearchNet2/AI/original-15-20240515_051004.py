
        client = self.get_conn()
        parent = ProductSearchClient.location_path(project_id, location)
        product = ProductSearchClient.product_path(project_id, location)
        reference_image_path = ProductSearchClient.reference_image_path(
            project_id, location, product_id, reference_image
        )
        reference_image_create_op = self.get_conn().create_reference_image(
            parent=parent,
            product=product,
            reference_image=reference_image,
            reference_image_id=reference_image_id