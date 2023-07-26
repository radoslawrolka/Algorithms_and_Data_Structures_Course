# time: O( len^2*n )
def prom(tab, lenght):
    n = len(tab)
    cache = [[[-1]*(lenght+1) for _ in range(lenght+1)] for _ in range(n)]

    def f(ind, l, p):
        nonlocal n, cache, tab
        if ind == n:
            return 0
        if cache[ind][l][p] != -1:
            return cache[ind][l][p]

        if tab[ind] > l and tab[ind] > p:
            cache[ind][l][p] = 0
            return 0

        if tab[ind] > l:
            cache[ind][l][p] = f(ind+1, l, p-tab[ind]) + 1
        elif tab[ind] > p:
            cache[ind][l][p] = f(ind+1, l-tab[ind], p) + 1
        else:
            a = f(ind+1, l, p-tab[ind]) + 1
            b = f(ind+1, l-tab[ind], p) + 1
            cache[ind][l][p] = max(a, b)
        return cache[ind][l][p]

    f(0, lenght, lenght)
    print(*cache, sep="\n")
    return cache[0][lenght][lenght]