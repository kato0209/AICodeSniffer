
        if not bucket:
            raise ValueError("Must provide bucket")
        if not key:
            raise ValueError("Must provide key")
        if not os.path.exists(path):
            raise ValueError("Local file does not exist")
        if not os.path.isdir(path):
            raise ValueError("Local directory does not exist")
        if not os.path.exists(os.path.join(path, key)):
            raise