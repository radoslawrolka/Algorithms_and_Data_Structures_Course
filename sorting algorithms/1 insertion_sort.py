# time - O(n^2)
# memory - O(1)

def insertion_sort(T):
    for i in range(1, len(T)):
        value = T[i]
        j = i-1
        while j >= 0 and value < T[j]:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = value
        print(T)


X = [9,7,2,5,3,2]
print(insertion_sort(X))
