"Shortest substring containing all vowels"

def shortestSubstring(s1, s2):
    required = set(s1)
    left = 0
    count = {}
    formed = 0
    res = float('inf')

    for right in range(len(s2)):
        ch = s2[right]
        if ch in required:
            count[ch] = count.get(ch, 0) + 1
            if count[ch] == 1:
                formed += 1

        while formed == len(required):
            res = min(res, right - left + 1)

            if s2[left] in count:
                count[s2[left]] -= 1
                if count[s2[left]] == 0:
                    formed -= 1

            left += 1

    return res if res != float('inf') else -1