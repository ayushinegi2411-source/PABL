"""You are given two arrays a[] and b[], return the Union of both the arrays in any order"""

def union_arrays(a, b):
    seen = {}
    result = []

    for x in a:
        if x not in seen:
            seen[x] = True
            result.append(x)

    for x in b:
        if x not in seen:
            seen[x] = True
            result.append(x)

    return result

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

print(union_arrays(a,b))