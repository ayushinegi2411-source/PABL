#Given an array arr and a number k. One can apply a swap operation on the array any
#number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find
#the minimum number of swaps required to bring all the numbers less than or equal
#to k together, i.e. make them a contiguous subarray.

def min_swaps(arr, k):
    n = len(arr)

    # Step 1: Count good elements
    good = sum(1 for x in arr if x <= k)

    # Step 2: Count bad elements in first window
    bad = sum(1 for x in arr[:good] if x > k)

    min_swaps = bad

    # Step 3: Slide window
    for i in range(good, n):
        # remove element going out
        if arr[i - good] > k:
            bad -= 1

        # add new element
        if arr[i] > k:
            bad += 1

        min_swaps = min(min_swaps, bad)

    return min_swaps

arr = [2, 1, 5, 6, 3]
k = 3
print(min_swaps(arr, k))