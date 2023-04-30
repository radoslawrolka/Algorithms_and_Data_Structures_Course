# [ O(V+E) ]
def DFS_array(graph):
    n = len(graph)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    processing = [None for _ in range(n)]
    low = [None for _ in range(n)]
    bridges = []
    time = 0

    def visit(graph, vertex):
        nonlocal time
        time += 1
        processing[vertex] = time
        low[vertex] = time
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                parent[neighbour] = vertex
                visit(graph, neighbour)

        for neighbour in graph[vertex]:
            if parent[neighbour] == vertex: # min-kid-rule
                if low[neighbour] < low[vertex]:
                    low[vertex] = low[neighbour]
            if parent[vertex] != neighbour: # min-back-edge-rule
                if low[neighbour] < low[vertex]:
                    low[vertex] = low[neighbour]

        if low[vertex] == processing[vertex] and parent[vertex] is not None:
            bridges.append((vertex, parent[vertex]))

    for i in range(n):
        if not visited[i]:
            visit(graph, i)

    return bridges


def find_bridges(graph):
    return DFS_array(graph)
