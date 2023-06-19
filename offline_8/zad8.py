# Radosław Rolka
from zad8testy import runtests

"""
Na początku zbieramy i zapisujemy wszyskie plamy ropy (gather) w najwcześniej występującym miejscu do zebrania (street)
oraz zapisujemy indeks miejsca do places.
Następnie przechodzimy po każdym polu 'places' i dodajemy do kolejki priorytetowej rope i razie potrzeby bierzemy 
'zachłannie' najwieksza mozliwa plame dotychczas spotkaną.
złożoność: O( n^2 )
"""

from collections import deque
from queue import PriorityQueue


def plan(map):
    y = len(map)
    x = len(map[0])
    street = [0] * x
    places = []

    def gather(main, x0):
        nonlocal y, x, street
        que = deque()
        que.append((x0, 0))

        while len(que) != 0:
            point_x, point_y = que.pop()
            # lewo
            new = point_x - 1
            if new >= 0 and map[point_y][new] > 0:
                street[main] += map[point_y][new]
                map[point_y][new] = 0
                que.append((new, point_y))

            # prawo
            new = point_x + 1
            if new < x and map[point_y][new] > 0:
                street[main] += map[point_y][new]
                map[point_y][new] = 0
                que.append((new, point_y))

            # gora
            new = point_y - 1
            if new >= 0 and map[new][point_x] > 0:
                street[main] += map[new][point_x]
                map[new][point_x] = 0
                que.append((point_x, new))

            # dol
            new = point_y + 1
            if new < y and map[new][point_x] > 0:
                street[main] += map[new][point_x]
                map[new][point_x] = 0
                que.append((point_x, new))

        places.append(main)

    for i in range(x - 1):
        if map[0][i] != 0:
            street[i] += map[0][i]
            map[0][i] = 0
            gather(i, i)

    stop = 1
    index = 1
    need = x - 1
    fuel = street[0]
    que = PriorityQueue()
    while fuel < need:
        while index < len(places) and places[index] <= fuel:
            que.put(-street[places[index]])
            index += 1
        fuel -= que.get()
        stop += 1

    return stop


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
