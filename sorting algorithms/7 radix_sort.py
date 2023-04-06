# time - O(n)
# memory - O(n)


def count_sort(T, exp):
    n = len(T)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = T[i]//exp
        count[index%10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = T[i] // exp
        output[count[index % 10] - 1] = T[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(T)):
        T[i] = output[i]


def radix_sort(T):
    max1 = max(T)
    exp = 1
    while max1/exp >= 1:
        count_sort(T, exp)
        exp *= 10


X = [5,3,6,9,2,1,9,4,7]
print(X)
print(radix_sort(X))
print(X)
