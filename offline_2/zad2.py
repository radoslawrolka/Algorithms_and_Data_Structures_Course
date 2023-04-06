# Radoslaw Rolka
from zad2testy import runtests

"""Sortujemy tablice heapsortem, i w momencie znajdywania najwiekszej wartosci dodajemy ja do sumy (tylko jesli jest 
wieksza od zera po odjeciu roztopionego sniegu) """


def heapify(T, n, i=0):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and T[largest] < T[left]:
        largest = left

    if right < n and T[largest] < T[right]:
        largest = right

    if largest != i:
        T[i], T[largest] = T[largest], T[i]
        heapify(T, n, largest)


def build_heap(T):
    n = len(T)
    for i in range((n - 2) // 2, -1, -1):
        heapify(T, n, i)


def heap_sort(T):
    suma = 0
    dni = 0
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        if T[i] - dni > 0:
            suma += T[i] - dni
            dni += 1
        else:
            return suma
        heapify(T, i, 0)


def snow(T):
    return heap_sort(T)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
