# vertex u,v are S-C-C when exist path u->v and v->u [ O(V+E) ]
def DFS_array(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    processing = [None for _ in range(n)]
    time = 0

    def visit(graph, vertex):
        nonlocal time
        time += 1
        processing[vertex] = (time, vertex)
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visit(graph, neighbour)

    for i in range(n):
        if not visited[i]:
            visit(graph, i)
    return processing

def reverse_edges(graph):
    n = len(graph)
    rev = [[] for _ in range(n)]
    for i in range(n):
        for vertex in graph[i]:
            rev[vertex].append(i)
    return rev

def DFS_SCC(graph, order_list):
    n = len(graph)
    visited = [False for _ in range(n)]
    result = []

    def visit(graph, vertex):
        visited[vertex] = True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                res.append(neighbour)
                visit(graph, neighbour)

    for i in order_list:
        if not visited[i[1]]:
            res = [i[1]]
            visit(graph, i[1])
            result.append(res)

    return result

def strongly_connected_component(graph):
    processed = DFS_array(graph)
    processed.sort()
    rev_graph = reverse_edges(graph)
    return DFS_SCC(rev_graph, processed)
