from kol1testy import runtests

"""
RADOSLAW ROLKA
Algorytm tworzy listę pierwszego przedzialu, sortuje ja i dodaje k-ty element do sumy. 
Nastepnie w petli dla kolejnych przedialow: usuwa z listy element ktory nie znajduje sie w kolejnym przedziale,
insertuje ten ktory wchodzi z zachowaniem posortowania listy i dodaje k-ty element do sumy.
Zlozonosc: O(np)
"""

def partition(T, first, last):
    pivot = T[last]
    i = first - 1
    for j in range(first, last):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[last] = T[last], T[i + 1]
    return i + 1

def quicksort(T, first, last):
    if first < last:
        pi = partition(T, first, last)
        quicksort(T, first, pi - 1)
        quicksort(T, pi + 1, last)

def insert(T):
    for i in range(len(T)-1):
        if T[-1] < T[i]:
            T[i], T[-1] = T[-1], T[i]


def ksum(T, k, p):
    n = len(T)

    tab = T[:p]
    quicksort(tab, 0, p - 1)
    suma = tab[p - k]

    for i in range(0, n - p):
        tab.remove(T[i])
        tab.append(T[i + p])
        insert(tab)
        suma += tab[p-k]

    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
