# taking the most valuable item by price/weight, we can take scrap of the item.
from queue import PriorityQueue
def gkp(weight_limit, prices, weights):
    n = len(prices)
    result = 0

    que = PriorityQueue()
    for i in range(n):
        que.put((-prices[i]/weights[i], weights[i]))

    for i in range(n):
        worth, weight = que.get()
        if weight < weight_limit:
            weight_limit -= weight
            result -= worth*weight
        else:
            result -= worth*weight_limit
            break

    return result

print(gkp(9, [40, 60, 150, 75], [4, 2, 3, 3]))  # 295
