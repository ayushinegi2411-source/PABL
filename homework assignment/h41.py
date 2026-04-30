"Sort by Frequency"

from collections import Counter

def sortByFreq(s):
    freq = Counter(s)
    return ''.join(sorted(s, key=lambda x: (freq[x], x)))