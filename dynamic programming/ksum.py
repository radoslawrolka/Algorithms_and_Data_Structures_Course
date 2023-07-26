# time O( n*k )
# lowest sum with taking a number from each k-lenght interval
def ksuma(T, k):
    n = len(T)
    result = [0 for _ in range(n)]

    for i in range(k):
        result[i] = T[i]

    for i in range(k, n):
        result[i] = T[i] + min(result[i-k:i])

    return min(result[n-k:n])