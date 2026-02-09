#Given an array of integers nums and an integer target, return indices of the two 
#numbers such that they add up to target. 
#You may assume that each input would have exactly one solution, and you may 
#not use the same element twice. 
#You can return the answer in any order. 
  
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums,target))