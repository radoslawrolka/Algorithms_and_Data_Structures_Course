# Radoslaw Rolka
from zad6testy import runtests

"""
Najpierw przydzielamy osobom po pierwszej możliwej maszynie (jesli to możliwe).
W kolejnej petli dla kazdego nieprzydzielonego czlowieka szukamy sciezki powiekszajacej (augumenting),która znajduje możliwe 
 przepięcie, aby powiekszyć ilość dopasowań. Jeśli ją znajdziemy to zwiekszamy counter o 1.

Augumenting : sprawdzamy kazda dostepna maszyne dla 'index', ktora nie jest zajęta przez inne osoby. 
  Następnie szukamy rekurencyjnie wolnej maszyny, albo odpalamy poszukiwanie dla operatora zajetej maszyny.
  Jeśli znajdziemy to zwracamy True i zamieniamy przypisania 'assign_m' i 'assign_p', w przeciwnym wypadku zwracamy False. 

Złożoność: O( V^2 )
"""


def augumenting(index, people, assign_m, assign_p, visited_m):
    for machine in people[index]:
        if not visited_m[machine]:
            visited_m[machine] = True
            if assign_m[machine] is None or augumenting(assign_m[machine], people, assign_m, assign_p, visited_m):
                assign_m[machine] = index
                assign_p[index] = machine
                return True
    return False


def binworker(people):
    V = len(people)
    counter = 0
    assign_m = [None] * V
    assign_p = [None] * V

    for i in range(V):
        for j in people[i]:
            if assign_m[j] is None:
                assign_m[j] = i
                assign_p[i] = j
                counter += 1
                break

    for i in range(V):
        if assign_p[i] is None:
            visited_m = [False] * V
            if augumenting(i, people, assign_m, assign_p, visited_m):
                counter += 1

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)
