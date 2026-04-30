"Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value."
"If target is not found in the array, return [-1, -1]."
"You must write an algorithm with O(log n) runtime complexity."

def searchRange(nums, target):
    def findLeft():
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid-1
            else:
                l = mid+1
            if nums[mid] == target:
                res = mid
        return res

    def findRight():
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= target:
                l = mid+1
            else:
                r = mid-1
            if nums[mid] == target:
                res = mid
        return res

    return [findLeft(), findRight()]