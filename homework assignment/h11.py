#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

def is_subset(a, b):
    freq = {}

    # Count elements of a
    for num in a:
        freq[num] = freq.get(num, 0) + 1

    # Check elements of b
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1

    return True

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
print(is_subset(a,b))