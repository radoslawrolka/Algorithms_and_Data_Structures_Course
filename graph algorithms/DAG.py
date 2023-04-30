# DAG - Directed Acyclic Graph [ O(V+E) ]
def DAG(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    processing = [None for _ in range(n)]
    position = n-1

    def visit(graph, vertex):
        nonlocal position
        visited[vertex] = True

        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visit(graph, neighbour)
        processing[position] = vertex
        position -= 1

    for i in range(n):
        if not visited[i]:
            visit(graph, i)

    return processing
