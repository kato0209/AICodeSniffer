
    res = False
    if _default_settings_path == _settings_path:
        return res

    for src in list(_default_settings_path.glob('**/*.json')):
        dest = _settings_path / src.relative_to(_default_settings_path)
        if not force and dest.exists():
            continue
        res = True
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dest)
    return res