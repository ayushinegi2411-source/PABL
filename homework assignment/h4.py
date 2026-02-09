# Given a sorted array of distinct integers and a target value, return the index if the 
#target is found. If not, return the index where it would be if it were inserted in 
#order. 

def index_val(num,target):
    l, r = 0, len(num) - 1

    while l <= r:
        m = (l + r) // 2
        if num[m] == target:
            return m
        if num[m] < target:
            l = m + 1
        else:
            r = m - 1

    return l

num = [1,3,5,6]
target =  5

print(index_val(num,target))