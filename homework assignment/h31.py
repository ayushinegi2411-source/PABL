"you are given an integer array arr[ ]. For every element in the array, your task is to"
"determine its Previous Smaller Element (PSE)."
"The Previous Smaller Element (PSE) of an element x is the first element that appears to"
"the left of x in the array and is strictly smaller than x."
"Note: If no such element exists, assign -1 as the PSE for that position."

def prevSmaller(arr):
    stack = []
    res = []

    for x in arr:
        while stack and stack[-1] >= x:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(x)

    return res