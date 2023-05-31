def DFS(G, points):
    V = len(G)
    parent = [None for _ in range(V)]
    visited = [False for _ in range(V)]
    d = [None for _ in range(V)]
    low = [None for _ in range(V)]
    time = 0

    def DFSVisit(G, u):
        nonlocal time
        time += 1
        d[u] = time
        low[u] = time
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v)

        for v in G[u]:
            if parent[u] != v:
                if low[v] < low[u]:
                    low[u] = low[v]
            if parent[v] == u:
                if low[v] < low[u]:
                    low[u] = low[v]

    for u in range(V):
        if not visited[u]:
            DFSVisit(G, u)

    childs = 0

    for v in G[0]:
        if parent[v] == 0:
            childs += 1

    if childs >= 2:
        points.append(0)

    for u in range(1, V):
        for v in G[u]:
            if parent[v] == u and low[v] >= d[u]:
                points.append(u)
                break


def art_points(G):
    points = []

    DFS(G, points)

    return points

G = [[1,2,5],
     [2,0],
     [0,1,3,4],
     [4,2],
     [2,3],
     [0,6],
     [5]]
print(art_points(G))
