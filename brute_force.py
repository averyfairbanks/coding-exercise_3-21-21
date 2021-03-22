def times_repeated(s, t):
    times = 1

    # first check if s contains all chars in t
    if not contains_chars(s, t):  # O(m * n)
        return -1

    while not is_substring(s * times, t):  # O(k^2 * mn)
        times += 1
    return times


def contains_chars(s, t):
    for ch in t:
        if s.find(ch) == -1:
            return False
    return True


# checks if all chars in t are in s IN ORDER
# exits when end of t is reached
def is_substring(s, t):
    t_idx = 0
    for ch in s:
        if ch == t[t_idx]:
            t_idx += 1
            if t_idx == len(t):
                return True

    return False
