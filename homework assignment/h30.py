"You are given an array arr[] of size n , where arr[i] denotes the range of working hours"
"a person at position i can cover."
"• If arr[i] ≠ -1, the person at index i can work and cover the time interval [i -arr[i], i + arr[i]]."
"• If arr[i] = -1, the person is unavailable and cannot cover any time."
"The task is to find the minimum number of people required to cover the entire working"
"day from 0 to n - 1. If it is not possible to fully cover the day, return -1."

def minSprinklers(arr):
    n = len(arr)
    intervals = []

    for i in range(n):
        if arr[i] != -1:
            intervals.append((max(0, i-arr[i]), min(n-1, i+arr[i])))

    intervals.sort()
    
    res = 0
    i = 0
    end = 0
    farthest = 0

    while end < n-1:
        while i < len(intervals) and intervals[i][0] <= end:
            farthest = max(farthest, intervals[i][1])
            i += 1
        
        if farthest == end:
            return -1
        
        res += 1
        end = farthest

    return res