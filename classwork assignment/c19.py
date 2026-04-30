"You are given an array arr[]. The task is to determine whether the array contains a 132"
"pattern, i.e., three indices i, j and k such that i < j < k , arr[i] < arr[j] >arr[k] and arr[i] < arr[k]."
"Return true if such a triplet exists, otherwise return false."

def find132pattern(nums):
    stack = []
    third = float('-inf')

    for i in range(len(nums)-1, -1, -1):
        if nums[i] < third:
            return True
        while stack and nums[i] > stack[-1]:
            third = stack.pop()
        stack.append(nums[i])

    return False