# Radoslaw Rolka
from zad4testy import runtests
from collections import deque
"""
przechodze BFS'em orginalny graf i zapisuje wyniki. Nastepnie usuwam po kolei kazda krawedz najkrotszej sciezki
i sprawdzam zmiany w BFS'ie. Jesli nowa sciezka jest dluzsza to ja zwracam, jesli nie to dodaje usunieta krawedz,
usuwam kolejna itd.
Zlozonosc: O(V)
"""


def BFS_shortest_path(graph, start, end):
    n = len(graph)
    que = deque()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    distance = [0 for _ in range(n)]

    visited[start] = True
    que.append(start)
    while len(que) != 0:
        vertice = que.popleft()
        for i in range(len(graph[vertice])):
            neighbour = graph[vertice][i]
            if not visited[neighbour]:
                visited[neighbour] = True
                distance[neighbour] = distance[vertice] + 1
                parent[neighbour] = vertice
                que.append(neighbour)
    path = []
    point = end
    while point != start:
        if point is None:
            return [], -1
        path.append([point, parent[point]])
        point = parent[point]
    return path, len(path)


def longer(graph, start, end):
    broken_path = 0
    main_path, main_distance = BFS_shortest_path(graph, start, end)

    for i in range(main_distance):
        missing_path = main_path[i]
        graph[missing_path[0]].remove(missing_path[1])
        graph[missing_path[1]].remove(missing_path[0])
        new_path, new_distance = BFS_shortest_path(graph, start, end)
        if new_distance > main_distance:
            return missing_path
        elif new_distance == -1:
            broken_path = missing_path
        graph[missing_path[0]].append(missing_path[1])
        graph[missing_path[1]].append(missing_path[0])

    return None if broken_path == 0 else broken_path


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
