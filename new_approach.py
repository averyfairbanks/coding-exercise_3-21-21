def times_repeated(s, t):
    d = get_dict(s, t)

    times = 1
    curr_idx = 0
    for ch in t:
        if not d[ch]:
            return -1

        flag = True
        for i in d[ch]:
            if i >= curr_idx:
                curr_idx = i
                flag = False
                break

        if flag:
            times += 1
            curr_idx = d[ch][0]

    return times


def get_dict(s, t):
    d = dict()
    for ch in t:
        if ch not in d:
            d[ch] = []

    for i in range(len(s)):
        if s[i] in d:
            d[s[i]].append(i)

    return d
