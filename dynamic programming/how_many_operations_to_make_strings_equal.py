def napraw(s, t):
    n = len(s)
    m = len(t)

    # create 2d array
    # dp[i][j] = minimum number of characters to change
    # to make s[:i] equal to t[:j]
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # initialize first row and column
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    # fill the rest of the array
    for i in range(1, n+1):
        for j in range(1, m+1):
            # if the last characters are equal
            # then we don't have to change anything
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # otherwise we have to change the last character
            # and we have to choose the minimum of the following:
            # 1. change the last character of s
            # 2. change the last character of t
            # 3. change the last character of both s and t
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[n][m]