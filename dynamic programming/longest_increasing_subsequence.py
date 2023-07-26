# time: O( n^2 )
def lis(tab):
    n = len(tab)
    result = [1]*n
    parent = [-1]*n

    for i in range(1, n):
        for j in range(i):
            if tab[j] < tab[i] and result[j]+1 > result[i]:
                parent[i] = j
                result[i] = result[j] + 1

    return max(result), parent

#time: O( nlogn)
def binary_search(arr, val):
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if val > arr[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx  # It will never exceed the left side of an array


def lis(arr):
    if len(arr) < 2:
        return len(arr)

    n = len(arr)
    last = []

    for i in range(n):
        j = binary_search(last, arr[i])
        if j == len(last):
            last.append(arr[i])
        else:
            last[j] = arr[i]

    print(last)
    return len(last)
    
