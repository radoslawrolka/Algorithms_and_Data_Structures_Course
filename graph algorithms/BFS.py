from queue import Queue

# BFS - Breadth-First Search

# reprezentacja macierzowa [ O(V^2) ]
def BFS_matrix(graph, start):
    n = len(graph)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]

    que = Queue()
    que.put(start)

    visited[start] = True
    distance[start] = 0

    while not que.empty():
        vertex = que.get()
        for i in range(n):
            if graph[vertex][i] == 1 and not visited[i]:
                visited[i] = True
                distance[i] = distance[vertex] + 1
                parent[i] = vertex
                que.put(i)
    return distance, parent, visited

# reprezentacja list sasiedztwa [ O(V+E) ]
def BFS_array(graph, start):
    n = len(graph)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]

    que = Queue()
    que.put(start)

    visited[start] = True
    distance[start] = 0

    while not que.empty():
        vertex = que.get()
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                distance[neighbour] = distance[vertex] + 1
                parent[neighbour] = vertex
                que.put(neighbour)
    return distance, parent, visited
