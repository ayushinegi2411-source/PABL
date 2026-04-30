"Lexicographically Largest String After K Deletions"

def largestString(s, k):
    stack = []

    for ch in s:
        while stack and k > 0 and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)

    return ''.join(stack[:len(stack)-k])