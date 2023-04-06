import math


def parent(i):
    return math.floor((i - 1) / 2)


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


# usuwa max wartosc z kopca
# time - O(logn) [całosc to heapify, reszta to czas staly]
def heap_extract_max(T):
    n = len(T)
    max_val = T[0]
    T[0] = T[n - 1]
    n -= 1
    heapify(T, n, 0)
    return max_val


# wstawianie do kopca
def heap_insert(T, value):
    T = T + [None]
    i = len(T) - 1
    while i > 0 and T[parent(i)] < value:
        T[i] = T[parent(i)]
        i = parent(i)
    T[i] = value
    return T


def build_heap_by_inserting(T):
    W = []
    for i in range(len(T)):
        W = heap_insert(W, T[i])
    return W

x = [9,2,34,5,7,8,4,7,876,5,4,3,2]
print(heap_extract_max(x))
