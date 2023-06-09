# time: O( n^2 )
def tsp(distances):
    n = len(distances)

    result = [[float('inf') for _ in range(n)] for _ in range(n)]
    result[0][1] = distances[0][1]

    def tspf(i, j):
        print(i,j)
        if result[i][j] != float('inf'):
            return result[i][j]
        if i == j - 1:
            best = float('inf')
            for k in range(j - 1):
                best = min(best, tspf(k, j - 1) + distances[k][j])
            result[j - 1][j] = best
        else:
            result[i][j] = tspf(i, j - 1) + distances[j - 1][j]
            
        return result[i][j]
