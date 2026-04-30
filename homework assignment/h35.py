"Given an array arr[] of size n, your task is to divide the array in two subsets such that the absolute difference between the sum of elements in the two subsets is equal"
"to zero (i.e., both subsets have the same sum)."
"• If n is even, both subsets must contain exactly n/2 elements."
"• If n is odd, one subset must contain (n-1)/2 elements and the other subset must contain (n+1)/2 elements."
"Note : If multiple answers exist, you may return any of them. The driver code will"
"check and print true if your partition is valid, otherwise false."
"It is guaranteed that there will always be atleast one valid partition."

def tugOfWar(arr):
    n = len(arr)
    total = sum(arr)
    best = float('inf')
    res = []

    def backtrack(i, subset):
        nonlocal best, res
        if len(subset) == n//2:
            s = sum(subset)
            diff = abs(total - 2*s)
            if diff < best:
                best = diff
                res = subset[:]
            return
        
        if i == n:
            return
        
        subset.append(arr[i])
        backtrack(i+1, subset)
        subset.pop()
        backtrack(i+1, subset)

    backtrack(0, [])
    return res