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
