#time: O( n^2 )
def matrices_mul_cost(A):
    if len(A) < 2: return 0

    n = len(A)
    F = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        F[i][i] = 0

    for i in range(n - 1):
        F[i][i + 1] = A[i][0] * A[i][1] * A[i + 1][1]

    for j in range(2, n):
        for i in range(n - j):
            for k in range(i, i + j):
                F[i][i + j] = min(F[i][i + j],
                                  F[i][k] + F[k + 1][i + j] + A[i][0] * A[k][1] * A[i + j][1])

    print(*F, sep='\n')

    return F[0][n - 1]
