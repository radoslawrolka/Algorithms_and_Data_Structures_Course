# time - O(n*logn)
# memory - O(n)


def partition(T, first, last):
    pivot = T[last]
    i = first-1
    for j in range(first, last):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[last] = T[last], T[i+1]
    return i+1


def quicksort(T, first=0, last=0):
    if first < last:
        pi = partition(T, first, last)
        quicksort(T, first, pi-1)
        quicksort(T, pi+1, last)


# max O(logn) dodatkowej pamięci
def quicksort_lessmemory(T, first=0, last=0):
    while first < last:
        pi = partition(T, first, last)
        quicksort(T, first, pi-1)
        first = pi + 1


X = [4,3,8,6,8,9,6]
print(X)
print(quicksort(X, 0, len(X)-1))
print(X)
