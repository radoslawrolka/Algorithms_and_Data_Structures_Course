from queue import PriorityQueue
def gas_station(graph, price_list, start, end, full, now):
    V = len(graph)
    cost = [[float('inf') for _ in range(full+1)] for _ in range(V)]
    cost[start] = [0 for _ in range(full+1)]
    parent = [[(None, 0) for _ in range(full+1)] for _ in range(V)]

    def dijkstra(start, end, full, cap_s):
        que = PriorityQueue()
        for i in range(0, full+1-cap_s):
            cost_s = price_list[start]*i
            que.put((cost_s, cap_s+i, start))

        while not que.empty():
            cost_v, cap_v, vertex = que.get()
            if vertex == end:
                break
            for kid, distance in graph[vertex]:
                if cap_v - distance >= 0:
                    cap_k = cap_v - distance
                    for i in range(0, full+1-cap_k):
                        cost_k = cost_v + price_list[kid]*i
                        if cost[kid][cap_k+i] > cost_k:
                            parent[kid][cap_k+i] = (vertex,cap_v)
                            cost[kid][cap_k+i] = cost_k
                            que.put((cost_k, cap_k+i, kid))

    dijkstra(start, end, full, now)

    path = []
    v = end
    f = cost[end].index(min(cost[end]))
    while v is not None:
        path.append(v)
        v, f = parent[v][f]
    return min(cost[end]), path[::-1]
