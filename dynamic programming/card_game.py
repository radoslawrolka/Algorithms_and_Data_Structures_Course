# max value of game where each player takes card from one side or another
def garek(T):
    n = len(T)
    cache = [[-1]*n for _ in range(n)]

    def f(a, b):
        nonlocal T, cache
        if cache[a][b] != -1:
            return cache[a][b]
        if a == b:
            cache[a][b] = (T[a], 0)
            return cache[a][b]
        elif a+1 == b:
            if T[a] > T[b]:
                cache[a][b] = (T[a], T[b])
                return cache[a][b]
            else:
                cache[a][b] = (T[b], T[a])
                return cache[a][b]
        else:
            left = f(a+1, b)
            right = f(a, b-1)
            if T[a] + left[1] > T[b] + right[1]:
                cache[a][b] = (left[1]+T[a], left[0])
            else:
                cache[a][b] = (right[1]+T[b], right[0])
            return cache[a][b]

    result = f(0, n-1)
    return result[0]
