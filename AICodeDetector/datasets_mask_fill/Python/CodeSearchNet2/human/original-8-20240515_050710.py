
        if conversation_key in self.conversations.keys():
            del self.conversations[conversation_key]
            log.info(f'Deleted conversation, key: {conversation_key}')