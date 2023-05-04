# Euler cycle, directed graph [ O(V^2) ]
def is_euler_cycle(graph):
    n = len(graph)
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += graph[i][j]
            sum -= graph[j][i] # not directed: this line does not exist
        if sum != 0: # not directed: if sum%2 =! 0:
            return False
    return True

def remove_edge(graph, start, end):
    graph[start][end] = 0
    # not directed: graph[end][start] = 0

def DFS(graph, path, guardian, start=0):
    n = len(graph)
    i = guardian[start]
    while guardian[start] < n:
        guardian[start] += 1
        if graph[start][i] == 1:
            remove_edge(graph, start, i)
            DFS(graph, path, guardian, i)
    path.append(start)

def euler_cycle(graph, start=0):
    n = len(graph)
    if not is_euler_cycle(graph):
        return None
    path = []
    guardian = [0 for _ in range(n)]
    DFS(graph, path, guardian, start)
    return path[::-1]
