# time: O( 2^n * n^2 )


import math
P = [(1, 2), (2, 3), (4, 5)]
n = len(P)
for k in range(n):
    i, j = P[k]
    if maxx < i:
        maxx = i
    if maxx < j:
        maxx = j

D = [[0 for a in range(maxx)] for _ in range(maxx)]

for k in range(n):
    i, j = P[k]
    D[i][j] = sqrt(i * i + j * j)

F = [[math.inf for j in range(n)] for i in range(n)]


def tspf(i, j, F, D):
    if F[i][j] != math.inf:
        return F[i][j]

    if i == j - 1:
        best = math.inf

        for k in range(j - 1):
            best = min(best, tspf(k, j - 1, F, D) + D[k][j])

        F[j - 1][j] = best

    else:
        F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]

    return F[i][j]