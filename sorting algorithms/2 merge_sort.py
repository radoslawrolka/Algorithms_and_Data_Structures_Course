# time - O(n*logn)
# memory - O(n)

def merge_sort(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        P = T[mid:]
        merge_sort(L)
        merge_sort(P)

        i, j = 0, 0
        k = 0
        while i < len(L) and j < len(P):
            if L[i] <= P[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = P[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1

        while j < len(P):
            T[k] = P[j]
            j += 1
            k += 1


X = [4, 6, 7, 3, 9, 2, 4, 6]
print(merge_sort(X))
print(X)
