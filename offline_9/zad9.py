# Radosław Rolka
from zad9testy import runtests

"""
Najpierw sprawdzamy ile trzeba zapłacić aby dostać się do i-tego pola,
Następnie ile musimy dopłacić, aby dojść z i-tego do końca.
A na końcu srawdzamy skoki wybierając najtańszy parking.
Złożoność: O( n*logn )
"""

from queue import PriorityQueue


def min_cost(dist_A, parking_cost, limit, dist_total):
    n = len(dist_A)

    road = [(0, 0)]
    for i in range(n):
        road.append((dist_A[i], parking_cost[i]))
    road.sort()
    road += [(dist_total, 0)]

    n += 2
    price_from_start = [0] * n
    price_to_end = [0] * n
    jump = [0] * n

    que = PriorityQueue()
    cost, distance, ind = 0, dist_total, n - 1
    for i in range(n - 1, -1, -1):
        while distance - road[i][0] > limit:
            cost, distance, ind = que.get()
        price_to_end[i] = cost + road[i][1]
        jump[i] = ind
        que.put((cost + road[i][1], road[i][0], i))

    que = PriorityQueue()
    cost, distance = 0, 0
    for i in range(n - 1):
        while road[i][0] - distance > limit:
            cost, distance = que.get()
        price_from_start[i] = cost + road[i][1]
        que.put((cost + road[i][1], road[i][0]))

    minimum = price_to_end[0]
    limit_new = 2 * limit
    que = PriorityQueue()
    j = 1
    for i in range(n - 1):
        j = max(jump[i], j)
        if j < n:
            while road[j][0] - road[i][0] <= limit_new:
                que.put((price_to_end[j], road[j][0]))
                j += 1
                if j == n:
                    break
        cost, distance = que.get()
        if cost + price_from_start[i] < minimum:
            minimum = cost + price_from_start[i]
        que.put((cost, distance))

    return minimum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)
