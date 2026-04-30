"you are given an array arr[ ], where arr[i] represents the height of the ith person standingin a line."
"A person i can see another person j if:"
"• height[j] < height[i],"
"• There is no person k standing between them such that height[k] ≥ height[i]."
"Each person can see in both directions (front and back)."
"Your task is to find the maximum number of people that any person can see (including themselves)."

def maxVisible(arr):
    n = len(arr)

    def count(arr):
        stack = []
        res = [0]*n

        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            res[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        return res

    left = count(arr)
    right = count(arr[::-1])[::-1]

    return max(left[i] + right[i] - 1 for i in range(n))