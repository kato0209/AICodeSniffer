
        if not s:
            return []
        if max_count < 1:
            return [s]
        if s[0] == s[-1]:
            return [s[:-1]]
        if s[0] == s[1]:
            return [s[1:]]
        if s[0] == s[2]:
            return [s[2:]]
        if