"You are given two binary strings s1 and s2 of equal length, and the task is to find"
"the minimum number of swaps required to make them identical. The only allowed"
"operation is swapping characters between the two strings (i.e., you can"
"swap s1[i] with s2[j], but not within the same string). If it is impossible to make the two"
"strings equal through such swaps, return -1"

def min_swaps(s1, s2):
    ones_s1 = s1.count('1')
    ones_s2 = s2.count('1')

    if ones_s1 + ones_s2 % 2 != 0:
        return -1

    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1

    return diff // 2