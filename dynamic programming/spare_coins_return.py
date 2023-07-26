#time: O( n*k )
def coin_master(coins, amount):
    result = [float('inf')]*(amount+1)

    for coin in coins:
        result[coin] = 1
        for i in range(coin, amount+1):
            result[i] = min(result[i], result[i-coin]+1)

    print(result)
    return result[amount]