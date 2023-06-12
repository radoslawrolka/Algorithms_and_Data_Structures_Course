# Radosław Rolka
from zad7testy import runtests
"""
legenda: -1 - pole niedostępne,
          0 - pole nieodwiedzone
          x - ile max komnat zostało odwiedzone przed
W algorytmie zaczynamy od przepisania wartosci z lewej kolumny powiększonych o 1. Nastepnie przechodzimy w gore i dol
i sprawdzamy czy da sie ta liczbe zwiekszyc poprzez uprzednie odwiedzenie komnat z dołu/góry. Po takim przejściu ustawiamy
result jako maksymalny rezultat z przejść [góra, dół]. Tablica result jest zmniejszona do wymiarow 2*n, wskaznik active-
to kolumna aktualnie wyliczana, prev- poprzednia. 
złożoność: O( n^2 )
"""

def maze(map):
    n = len(map)
    result = [[0, 0] for _ in range(n)]
    result_directed = [[0, 0] for _ in range(n)]
    active = True
    prev = False

    # pierwsza kolumna
    for y in range(1, n):
        if result[y-1][0] == -1 or map[y][0] == '#':
            result[y][0] = -1
        else:
            result[y][0] = result[y-1][0] + 1

    # cala macierz
    for x in range(1, n-1):

        # lewo
        for y in range(n):
            if result[y][prev] == -1 or map[y][x] == '#':
                result_directed[y][0] = -1
                result_directed[y][1] = -1
            else:
                new = result[y][prev] + 1
                result_directed[y][0] = new
                result_directed[y][1] = new

                # inkrementuj w dol
        for y in range(1, n):
            if map[y][x] == '#' or result_directed[y-1][0] == -1:
                continue
            new = result_directed[y-1][0] + 1
            if new > result_directed[y][0]:
                result_directed[y][0] = new

        # inkrementuj w gore
        for y in range(n-2, -1, -1):
            if map[y][x] == '#' or result_directed[y + 1][1] == -1:
                continue
            new = result_directed[y + 1][1] + 1
            if new > result_directed[y][1]:
                result_directed[y][1] = new

        # ustawianie max resulta
        for y in range(n):
            result[y][active] = max(result_directed[y])

        active = not active
        prev = not prev

    # ostatnia kolumna
    x = n-1
    # lewo
    for y in range(n):
        if result[y][prev] == -1 or map[y][x] == '#':
            result_directed[y][0] = -1
            result_directed[y][1] = -1
        else:
            new = result[y][prev] + 1
            result_directed[y][0] = new
            result_directed[y][1] = new
            result[y][active] = new
    # dol
    for y in range(1, n):
        if map[y][x] == '#' or result_directed[y - 1][0] == -1:
            continue
        new = result_directed[y - 1][0] + 1
        if new > result_directed[y][0]:
            result[y][active] = result_directed[y][0] = new

    if result[x][active] != 0:
        return result[x][active]
    else:
        return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
