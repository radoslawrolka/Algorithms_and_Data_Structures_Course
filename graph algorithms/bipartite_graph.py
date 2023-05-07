# BFS approach [ O(V+E) ]
from queue import Queue
def bipartite_BFS(graph):
    V = len(graph)
    visited = [False for _ in range(V)]
    colour = [0 for _ in range(V)]

    que = Queue()
    que.put((0, 1))

    visited[0] = True
    colour[0] = 1

    while not que.empty():
        vertex, col = que.get()
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                colour[neighbour] = col * (-1)
                que.put((neighbour, col * (-1)))
            else:
                if colour[vertex] == colour[neighbour]:
                    return False

    groups = [[], []]
    for i in range(V):
        if colour[i] == 1:
            groups[1].append(i)
        else:
            groups[0].append(i)
    return groups


# DFS approach [ O(V+E) ]
def bipartite_DFS(graph):
    V = len(graph)
    visited = [False for _ in range(V)]
    colour = [0 for _ in range(V)]
    colour[0] = 1
    flag = 0

    def visit(graph, vertex):
        nonlocal flag
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                colour[neighbour] = colour[vertex] * (-1)
                visit(graph, neighbour)
            else:
                if colour[vertex] == colour[neighbour]:
                    flag = 1
                    return False

    for i in range(V):
        if not visited[i]:
            visit(graph, i)

    if flag == 1:
        return False

    groups = [[], []]
    for i in range(V):
        if colour[i] == 1:
            groups[1].append(i)
        else:
            groups[0].append(i)

    return groups
