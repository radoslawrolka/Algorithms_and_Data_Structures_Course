from zad3testy import runtests

"""
Radoslaw Rolka
Sortujemy wszystkie slowa jednoczesnie obracajac tak, aby zaczynaly sie od wczesniejszej alfabetycznie litery
"""

def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while (True):
        i += 1
        while (arr[i] < pivot):
            i += 1

        j -= 1
        while (arr[j] > pivot):
            j -= 1

        if (i >= j):
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quicksort(T, first=0, last=0):
    if first < last:
        pi = partition(T, first, last)
        quicksort(T, first, pi)
        quicksort(T, pi+1, last)

def strong_string(T):
    n = len(T)
    for i in range(n):
        a, b = 0, len(T[i]) - 1
        while a < b:
            if T[i][a] > T[i][b]:
                T[i] = T[i][::-1]
            elif T[i][a] < T[i][b]:
                break
            else:
                a += 1
                b -= 1
    """
    dict = {}
    for i in range(n):
        if T[i] in dict.keys():
            dict[T[i]] += 1
        else:
            dict.update({T[i]: 1})

    return max(dict.values())
    """
    quicksort(T, 0, n-1)

    strong = strongest = 1
    for i in range(1, n):
        if T[i] == T[i-1]:
            strong += 1
        else:
            if strongest < strong:
                strongest = strong
            strong = 1
    if strongest < strong:
        return strong
    return strongest

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)


