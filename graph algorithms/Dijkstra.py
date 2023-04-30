from queue import PriorityQueue
from math import inf

# reprezentacja macierzowa [ O(V^2) ]
def dijkstra_matrix(graph, start, end):
    n = len(graph)
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]

    que = PriorityQueue()
    que.put((0, start))
    distance[start] = 0

    while not que.empty():
        cost, vertex = que.get()
        if vertex == end:
            return distance[end], parent
        for kid in range(len(graph[vertex])):
            value = graph[vertex][kid]
            new_cost = cost + value
            if distance[kid] > new_cost:
                parent[kid] = vertex
                distance[kid] = new_cost
                que.put((new_cost, kid))
    return distance[end], parent

# reprezentacja listowa [ O(E*logV) ]
def dijkstra_array(graph, start, end):
    n = len(graph)
    distance = [inf for _ in range(n)]
    parent = [None for _ in range(n)]

    que = PriorityQueue()
    que.put((0, start))
    distance[start] = 0

    while not que.empty():
        cost, vertex = que.get()
        if vertex == end:
            return distance[end], parent
        for value, kid in graph[vertex]:
            new_cost = cost + value
            if distance[kid] > new_cost:
                parent[kid] = vertex
                distance[kid] = new_cost
                que.put((new_cost, kid))
    return distance[end], parent
