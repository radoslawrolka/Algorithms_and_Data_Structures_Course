# [ O(V*E) ] graph - edge-array: (start,end,value)
def bellman_ford(graph, num_of_vertex, start):
    def relax(fir, sec, val):
        if distance[sec] > distance[fir] + val:
            distance[sec] = distance[fir] + val
            parent[sec] = fir

    def is_negative_cycle(fir, sec, val):
        if distance[sec] <= distance[fir] + val:
            return True
        return False

    parent = [None for _ in range(num_of_vertex)]
    distance = [float('inf') for _ in range(num_of_vertex)]

    distance[start] = 0
    for i in range(num_of_vertex - 1):
        for first, second, cost in graph:
            relax(first, second, cost)

    for first, second, cost in graph:
        if not is_negative_cycle(first, second, cost):
            return "Negative cycle has been found"

    return distance, parent
