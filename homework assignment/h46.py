"Count Even Letters"

from collections import Counter

def countEven(s):
    freq = Counter(s)
    return sum(1 for v in freq.values() if v % 2 == 0)