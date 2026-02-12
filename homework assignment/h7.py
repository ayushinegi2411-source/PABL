#You are given an array arr[] of non-negative numbers. Each number tells you the maximum 
#number of steps you can jump forward from that position.

def min_jumps(arr):
    n = len(arr)
    
    if n <= 1:
        return 0
    
    if arr[0] == 0:
        return -1

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

            # If we can't move further
            if current_end <= i:
                return -1

    return jumps

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_jumps(arr))