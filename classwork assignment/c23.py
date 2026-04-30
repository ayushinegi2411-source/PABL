"Winner of an election"

from collections import Counter

def winner(arr):
    freq = Counter(arr)
    max_votes = max(freq.values())

    candidates = [k for k, v in freq.items() if v == max_votes]
    return [min(candidates), str(max_votes)]