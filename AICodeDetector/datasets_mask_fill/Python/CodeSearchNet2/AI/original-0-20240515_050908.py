
        return {
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "attachments": self.attachments,
            "ts": int(time.time()),
            "attachments_count": len(self.attachments),
            "attachments_last_ts": self.attachments[-1]["ts"],
            "attachments_last_message": self.attachments[-1]["message"],
            "attachments_last_user": self.attachments[-1]["user"],
 