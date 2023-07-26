# write an algorirthm that finds max flow in a graph from source to sink
def max_flow(graph, source, sink):
    V = len(graph)
    flow = 0

    def bfs(graph, source, sink):
        visited = [False] * V
        visited[source] = True
        queue = [source]
        paths = {source: []}
        while queue:
            u = queue.pop(0)
            for v in range(V):
                if not visited[v] and graph[u][v] > 0:
                    paths[v] = paths[u] + [(u, v)]
                    visited[v] = True
                    queue.append(v)
                    if v == sink:
                        return paths[v]
        return None

    while True:
        # find an augmenting path
        path = bfs(graph, source, sink)
        if path is None:
            break
        # find the maximum flow that can be sent
        # over the path we found
        path_flow = min(graph[u][v] for u, v in path)
        # update residual capacities of the edges and
        # reverse edges along the path
        for u, v in path:
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
        flow += path_flow

    return flow
