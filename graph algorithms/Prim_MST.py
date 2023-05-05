# Prim's Algorithm - MST (minimal spanning trees) [ O(E*logV) ]

from queue import PriorityQueue
def Prim_MST(graph, start):
    V = len(graph)
    parent = [None for _ in range(V)]
    visited = [False for _ in range(V)]
    cost = [float('inf') for _ in range(V)]

    que = PriorityQueue()
    que.put((0, start))
    cost[start] = 0

    while not que.empty():
        value, vertex = que.get()
        if visited[vertex]:
            continue
        for neighbour, val in graph[vertex]:
            if val < cost[neighbour]:
                cost[neighbour] = val
                parent[neighbour] = vertex
                que.put((cost[neighbour], neighbour))

    MST = []
    for i in range(1, V):
        MST.append((parent[i], i))

    return MST
