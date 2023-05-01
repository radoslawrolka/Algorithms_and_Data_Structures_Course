# Radoslaw Rolka
from zad5testy import runtests
from queue import PriorityQueue
from math import inf

"""
Zamieniam reprezentacje listowa, na reprezentacje sasiadow. Nastepnie tworze polaczenia miedzy planetami z zakrzywieniami o czasie rownym '0'.
I uruchamiam algorytm dijkstry.
Zlozonosc: O(E + S + E*logV)
"""


def to_neighbour_list(graph, number_of_vertex):
    tab = [[] for _ in range(number_of_vertex)]
    for a, b, val in graph:
        tab[a].append((val, b))
        tab[b].append((val, a))
    return tab


def dijkstra(graph, start, end, number_of_vertex):
    distance = [inf for _ in range(number_of_vertex)]
    que = PriorityQueue()
    distance[start] = 0
    que.put((0, start))

    while not que.empty():
        cost, vertex = que.get()
        if vertex == end:
            return distance[end]
        for value, kid in graph[vertex]:
            if distance[kid] > cost + value:
                distance[kid] = cost + value
                que.put((cost + value, kid))
    return distance[end]


def spacetravel(number_of_planet, list_of_edges, list_of_strange_planets, start, end):
    list_of_edges = to_neighbour_list(list_of_edges, number_of_planet)

    main = list_of_strange_planets[0]
    for i in range(1, len(list_of_strange_planets)):
        new = list_of_strange_planets[i]
        list_of_edges[main].append((0, new))
        list_of_edges[new].append((0, main))

    distance = dijkstra(list_of_edges, start, end, number_of_planet)
    return distance if distance != inf else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
