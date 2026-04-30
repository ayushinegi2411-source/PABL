"Check if Permutation is Substring"

from collections import Counter

def checkInclusion(pat, txt):
    k = len(pat)
    pat_count = Counter(pat)
    window = Counter(txt[:k])

    if window == pat_count:
        return True

    for i in range(k, len(txt)):
        window[txt[i]] += 1
        window[txt[i-k]] -= 1

        if window[txt[i-k]] == 0:
            del window[txt[i-k]]

        if window == pat_count:
            return True

    return False