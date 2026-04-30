"Balancing Consonants and Vowels Ratio"

def countBalanced(arr):
    def val(s):
        v = set('aeiou')
        score = 0
        for ch in s:
            score += 1 if ch in v else -1
        return score

    prefix = {0: 1}
    curr = 0
    res = 0

    for s in arr:
        curr += val(s)
        res += prefix.get(curr, 0)
        prefix[curr] = prefix.get(curr, 0) + 1

    return res