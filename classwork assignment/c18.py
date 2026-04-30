"Given a matrix a of size n*m which represents a park, there is some construction work"
"needs to be done. You are also given q queries each query contains two"
"numbers R and C, For every query we need to construct a footpath in the Rth row"
"and Cth column, there is a cost of this construction, after the construction this path will"
"divide the park into sections, and the cost of the construction is"
"the sum of minimum value present in all the sections. You are asked to find this cost"
"for all the queries."
"Note: Elements present in queries array are according to 1-based indexing"

def footpathCost(mat, r, c):
    r -= 1
    c -= 1
    n, m = len(mat), len(mat[0])
    ans = 0

    sections = []

    # 4 quadrants
    sections.append([mat[i][j] for i in range(0, r) for j in range(0, c)])
    sections.append([mat[i][j] for i in range(0, r) for j in range(c+1, m)])
    sections.append([mat[i][j] for i in range(r+1, n) for j in range(0, c)])
    sections.append([mat[i][j] for i in range(r+1, n) for j in range(c+1, m)])

    for sec in sections:
        if sec:
            ans += min(sec)

    return ans