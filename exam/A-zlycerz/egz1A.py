# Radosław Rolka
from egz1Atesty import runtests

"""
Mamy 2 mapy jedna przed kradzieżą, druga po.
distances - ile trzeba wydać aby dojśc od startu do itego pola
distances_2 - ile trzeba wydać aby dojśc od konca do itego pola po kradziezy
wynik to dojscie do 'i' - kradzież złota z i + dojscie do konca
I tą formułę sprawdzamy dla każdego wierzhołka 'i'
złożoność: O( V^2*logV ) [ElogV -> E <= V^2]
"""

from queue import PriorityQueue
def gold(mapa, zloto, start, end, bribe):
    n = len(mapa)

    mapa_2 = [[(j[0], j[1] * 2 + bribe) for j in i] for i in mapa]

    def dijkstra_1(start, end):
        nonlocal mapa
        n = len(mapa)
        distance = [float('inf') for _ in range(n)]

        que = PriorityQueue()
        que.put((0, start))
        distance[start] = 0

        while not que.empty():
            cost, vertex = que.get()
            for kid, value in mapa[vertex]:
                new_cost = cost + value
                if distance[kid] > new_cost:
                    distance[kid] = new_cost
                    que.put((new_cost, kid))
        return distance

    def dijkstra_2(start, end):
        nonlocal mapa_2
        n = len(mapa_2)
        distance = [float('inf') for _ in range(n)]

        que = PriorityQueue()
        que.put((0, start))
        distance[start] = 0

        while not que.empty():
            cost, vertex = que.get()
            for kid, value in mapa_2[vertex]:
                new_cost = cost + value
                if distance[kid] > new_cost:
                    distance[kid] = new_cost
                    que.put((new_cost, kid))
        return distance

    distances = dijkstra_1(start, end)
    distances_2 = dijkstra_2(end, start)

    minimium = float('inf')
    for i in range(n):
        cost = distances[i] - zloto[i] + distances_2[i]
        if cost < minimium:
            minimium = cost

    return minimium

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)



