
    today = timezone.utcnow().replace(
        hour=hour,
        minute=minute,
        second=second,
        microsecond=microsecond)
    return today - timedelta(days=n)