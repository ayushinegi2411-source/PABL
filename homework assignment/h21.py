"Given an array of strings strs, group the anagrams together. You can return the answer in any order."

from collections import defaultdict

def groupAnagrams(strs):
    mp = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        mp[key].append(word)

    return list(mp.values())