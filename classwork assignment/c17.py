"Given a integer matrix (or 2D array) a[][] of dimensions n * m. Also, given another 2-D array query[][] of dimensions q * 4."
"For each index 0 < i < query.length, find the sum of all the elements of the rectangular"
"matrix whose top left corner is (query[i][0], query[i][1]) and bottom right corner is (query[i][2], query[i][3])."

def prefixSumMatrix(mat):
    n, m = len(mat), len(mat[0])
    pre = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            pre[i][j] = mat[i][j]
            if i > 0:
                pre[i][j] += pre[i-1][j]
            if j > 0:
                pre[i][j] += pre[i][j-1]
            if i > 0 and j > 0:
                pre[i][j] -= pre[i-1][j-1]
    return pre

def query(pre, r1, c1, r2, c2):
    res = pre[r2][c2]
    if r1 > 0:
        res -= pre[r1-1][c2]
    if c1 > 0:
        res -= pre[r2][c1-1]
    if r1 > 0 and c1 > 0:
        res += pre[r1-1][c1-1]
    return res