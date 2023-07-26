# time: O( n^2 )
def sum_to_t(array, T):
    n = len(array)
    result = [False]*(T+1)
    result[0] = True

    for i in array:
        for j in range(T, i-1, -1):
            if result[j-i]:
                result[j] = True

    return result[T]