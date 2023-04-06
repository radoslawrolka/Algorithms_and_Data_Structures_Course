# time - O(n*logn)+
# memory - O(n)

# buduje drzewo binarne z maxem w korzeniu, jeśli korzeń się zmienia
#   to heapif'ujemy poddrzewo
# dane wejściowe to tablica, len(T), i-ty indeks
# time - O(logn)
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


# tworzy kopiec (liście są mniejsze niż korzeń, ale nie posortowane)
# time - O(n)
def build_heap(T):
    n = len(T)
    for i in range((n-2)//2, -1, -1):
        heapify(T, n, i)


# posortowany kopiec
def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n - 1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)
    print(T)


X = [6, 9, 2, 4, 0, 1, 8, 5]
print(X)
print(heap_sort(X))
