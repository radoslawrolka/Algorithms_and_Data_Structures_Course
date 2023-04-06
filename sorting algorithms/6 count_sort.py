# time - O(n)
# memory - O(n)

# Tablica, wynikowa, k(maxvalue w T), C(ile powtorzen liczby, a potem ile <= i pozycja w W)
def count_sort(T):
    maks = max(T)
    Output = [0 for _ in range(len(T))]
    Count = [0 for _ in range(maks+1)]
    for i in range(len(T)):
        Count[T[i]] += 1
    for i in range(2, maks+1):
        Count[i] += Count[i-1]
    for i in range(len(T)-1, -1, -1):
        Output[Count[T[i]]-1] = T[i]
        Count[T[i]] -= 1
    return Output


X = [4,8,6,3,2,6,8,9,4]
print(X)
Y = count_sort(X)
print(Y)
