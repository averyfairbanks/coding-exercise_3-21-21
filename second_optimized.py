# m = len(s), n = len(t)
def times_repeated(s, t):
    if not contains_chars(s, t):  # O(m * n)
        return -1

    times = 0
    s_idx = 0
    t_idx = 0
    while t_idx < len(t): # O(m * n)
        i = s_idx

        times_on_enter = times
        while times <= times_on_enter + 1:
            if i == 0:
                times += 1

            if s[i] == t[t_idx]:
                t_idx += 1
                s_idx = (i + 1) % len(s)
                break
            i = (i + 1) % len(s)

    return times


def contains_chars(s, t):
    for ch in t:
        if s.find(ch) == -1:
            return False
    return True
