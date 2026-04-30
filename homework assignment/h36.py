"Given an array arr[] of integers and an integer k, select k elements from the array such"
"that the minimum absolute difference between any two of the selected elements"
"is maximized. Return this maximum possible minimum difference."

def maxMinDiff(arr, k):
    arr.sort()

    def can(d):
        count = 1
        last = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - last >= d:
                count += 1
                last = arr[i]
        return count >= k

    l, r = 0, arr[-1] - arr[0]
    ans = 0

    while l <= r:
        mid = (l+r)//2
        if can(mid):
            ans = mid
            l = mid+1
        else:
            r = mid-1

    return ans