"Given an integer array nums of unique elements, return all possible subsets (the powerset)."
"The solution set must not contain duplicate subsets. Return the solution in any order."

def subsets(nums):
    res = []

    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()

    backtrack(0, [])
    return res