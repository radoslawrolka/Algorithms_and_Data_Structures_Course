# DFS - Depth-First Search

# reprezentacja macierzowa [ O(V^2) ]
def DFS_matrix(graph):
    n = len(graph)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    processing = [None for _ in range(n)]
    time = 0

    def visit(graph, vertex):
        n = len(graph)
        nonlocal time
        time += 1
        processing[vertex] = time
        visited[vertex] = True
        for i in range(n):
            if not visited[i] and graph[vertex][i]:
                parent[i] = vertex
                visit(graph, i)

    for i in range(n):
        if not visited[i]:
            visit(graph, i)

    return processing, parent


# reprezentacja listowa [ O(V+E) ]
def DFS_array(graph):
    n = len(graph)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    processing = [None for _ in range(n)]
    time = 0

    def visit(graph, vertex):
        n = len(graph)
        nonlocal time
        time += 1
        processing[vertex] = time
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                parent[neighbour] = vertex
                visit(graph, neighbour)

    for i in range(n):
        if not visited[i]:
            visit(graph, i)

    return processing, parent
