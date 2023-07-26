# time: O( maxh*maxw*n )
def knucksack_2d(V, W, H, maxw, maxh):
    n = len(V)

    F = [[[0] * (maxh + 1) for _ in range(maxw + 1)] for _ in range(n)]  # f(i,w,h)
    parent = [[[[None] * 3 for _ in range(n)] for _ in range(maxh + 1)] for _ in range(maxw + 1)]

    # if czy miesci sie pierwszy
    for w in range(W[0], maxw + 1):
        for h in range(H[0], maxh + 1):
            F[0][w][h] = V[0]

    for w in range(maxw + 1):
        for h in range(maxh + 1):
            for i in range(1, n):
                F[i][w][h] = F[i - 1][w][h]
                parent[w][h][i] = (w, h, i - 1)
                if w - W[i] >= 0 and h - H[i] >= 0 and F[i][w][h] < F[i - 1][w - W[i]][h - H[i]] + V[i]:
                    F[i][w][h] = F[i - 1][w - W[i]][h - H[i]] + V[i]
                    parent[w][h][i] = (w - W[i], h - H[i], i - 1)

    maxv = 0
    maxwi, maxhi = None, None
    ind = None
    for w in range(maxw + 1):
        for h in range(maxh + 1):
            for i in range(n):
                if maxv < F[i][w][h]:
                    maxv = F[i][w][h]
                    maxwi, maxhi = w, h
                    ind = i

    path = []
    while parent[maxwi][maxhi][ind][0] != None and parent[maxwi][maxhi][ind][1] != None and parent[maxwi][maxhi][ind][
        2] != None:
        w, h = parent[maxwi][maxhi][ind][0:2]
        if w != maxwi and h != maxhi:
            path.append(ind)
        maxwi, maxhi, ind = parent[maxwi][maxhi][ind]

    return maxv, path
