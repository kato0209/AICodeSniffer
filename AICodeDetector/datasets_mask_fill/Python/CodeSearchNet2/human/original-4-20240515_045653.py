

    ds = datetime.strptime(ds, '%Y-%m-%d')
    if days:
        ds = ds + timedelta(days)
    return ds.isoformat()[:10]