# time: O( n * weight_limit )
# weights are sorted, price[i] is price of element i, that weights weight[i]
def knapsack(weight_limit, prices, weights):
    n = len(prices)
    result = [[0 for _ in range(weight_limit+1)] for _ in range(n)]
    parent = [[[None, None, False] for _ in range(weight_limit+1)] for _ in range(n)]

    for i in range(weights[0], weight_limit+1):
        result[0][i] = prices[0]
        parent[0][i] = [None, None, True]

    for i in range(weight_limit+1):
        for j in range(1, n):
            result[j][i] = result[j-1][i]
            parent[j][i] = [j-1, i, False]
            if i-weights[j] >= 0:
                # result[j][i] = max(result[j][i], result[j-1][i-weights[j]]+prices[j])
                if result[j][i] < result[j-1][i-weights[j]]+prices[j]:
                    result[j][i] = result[j-1][i-weights[j]]+prices[j]
                    parent[j][i] = [j-1, i-weights[j], True]

    stuff = []
    y,x = n-1, weight_limit
    while x is not None:
        if parent[y][x][2]:
            stuff.append(y)
        y,x,b = parent[y][x]

    return result[n-1][weight_limit], stuff

print(knapsack(5, [60, 90,100,120], [1,1,2,3]))
print(knapsack(15, [1,2,2,10,4], [1,1,2,4,12]))
