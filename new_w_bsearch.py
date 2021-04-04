def times_repeated(s, t):
    d = get_dict(s, t)

    times = 1
    curr_idx = 0
    for ch in t:
        if not d[ch]:
            return -1

        # modified binary search for next highest value
        inds = d[ch]
        if inds[-1] < curr_idx:
            curr_idx = -1
            break
        else:
            curr_idx = binary_search(curr_idx, inds)

        if curr_idx == -1:
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


# modified binary search for next highest value
def binary_search(idx, inds):
    if len(inds) == 1:
        if inds[0] > idx:
            return inds[0]
        else:
            return -1

    mid = len(inds) / 2
    if inds[mid] > idx:
        binary_search(idx, inds[0: mid + 1])
    elif inds[mid] < idx:
        binary_search(idx, inds[mid + 1:])
