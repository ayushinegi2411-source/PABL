"Given an array of distinct integers candidates and a target integer target, return a list of"
"all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order."
"The same number may be chosen from candidates an unlimited number of times."
"Two combinations are unique if the frequency of at least one of the chosen numbers is different."
"The test cases are generated such that the number of unique combinations that sum up"
"to target is less than 150 combinations for the given input"

def combinationSum(candidates, target):
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return res