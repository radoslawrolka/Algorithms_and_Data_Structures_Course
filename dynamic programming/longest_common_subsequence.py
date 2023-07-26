def longest_common_subsequence(A, B):
    n = len(A)
    m = len(B)
    result = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        if A[i] == B[0]:
            result[i][0] = 1
        else:
            result[i][0] = result[i - 1][0]

    for i in range(m):
        if A[0] == B[i]:
            result[0][i] = 1
        else:
            result[0][i] = result[0][i - 1]

    for i in range(1, n):
        for j in range(1, m):
            if A[i] == B[j]:
                result[i][j] = result[i - 1][j - 1] + 1
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])

    for i in range(n):
        print(result[i])
    return result[n - 1][m - 1]
