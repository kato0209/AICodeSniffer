
        client = self.get_conn()
        return client.search_detection(
            image=image, max_results=max_results, retry=retry, timeout=timeout, additional_properties=additional_properties
        )

    @GoogleCloudBaseHook.fallback_to_default_project_id
    def translate_image(
        self,
        image: str,
        source_language: str,
        target_language: str,
        retry: Optional[Retry] = None,
        timeout: Optional[float] = None,
        additional_properties: Optional[Dict] = None,
    ) -> Image: