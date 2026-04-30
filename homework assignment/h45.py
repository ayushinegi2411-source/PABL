"Count Unique Vowel Strings"

import math
from collections import Counter

def countVowelStrings(s):
    vowels = "aeiou"
    freq = Counter(s)

    counts = [freq[v] for v in vowels if freq[v] > 0]

    if not counts:
        return 0

    total_choices = 1
    for c in counts:
        total_choices *= c

    return total_choices * math.factorial(len(counts))