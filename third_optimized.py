def times_repeated(s, t):
    if not contains_chars(s, t):
            return -1

    times = 0
    i = 0
    for ch in t:
        times_on_enter = times
        while times <= times_on_enter + 1:
            if i == 0:
                times += 1
            if s[i] == ch:
                i = (i + 1) % len(s)
                break
            i = (i + 1) % len(s)

    return times


def contains_chars(s, t):
    d = set()
    for ch in s:
        if ch not in d:
            d.add(ch)

    for ch in t:
        if ch not in d:
            return False
    return True
