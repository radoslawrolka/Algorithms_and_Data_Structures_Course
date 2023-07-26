# time: O( n^2 )
def blocks(tab):
    n = len(tab)
    result = [float('inf')]*n
    result[0] = 0
    size = [[None, None]] * n
    size[0] = tab[0]

    for i in range(1, n):
        a, b = tab[i]
        counter = 0
        for j in range(i-1, -1, -1):
            if result[j] + counter < result[i]:
                a2, b2 = size[j]
                if a2<=a and b<=b2:
                    result[i] = result[j] + counter
                    size[i] = [a, b]
            counter += 1
        if result[i] == float('inf'):
            result[i] = i
            size[i] = tab[i]

    return result[n-1]
