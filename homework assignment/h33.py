"You are given an integer array arr[ ]. Your task is to count the number of subarrays"
"where the first element is the minimum element of that subarray."
"Note: A subarray is valid if its first element is not greater than any other element in that subarray."

def countSubarrays(arr):
    n = len(arr)
    res = 0

    for i in range(n):
        for j in range(i, n):
            if min(arr[i:j+1]) == arr[i]:
                res += 1

    return res