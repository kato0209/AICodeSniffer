
        payload = {}

        for key in [
            "message", "alias", "description", "responders",
            "visibleTo", "actions", "tags", "details", "entity",
            "source", "priority", "user", "note"
        ]:
            val = getattr(self, key)
            if val:
                payload[key] = val
      