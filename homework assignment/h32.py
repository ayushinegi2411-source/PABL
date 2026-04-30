"You are given an integer array arr[ ]. For every element in the array, your task is to"
"determine its Previous Greater Element (PGE)."
"The Previous Greater Element (PGE) of an element x is the first element that appears to"
"the left of x in the array and is strictly greater than x."
"Note: If no such element exists, assign -1 as the PGE for that position."

def prevGreater(arr):
    stack = []
    res = []

    for x in arr:
        while stack and stack[-1] <= x:
            stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(x)

    return res