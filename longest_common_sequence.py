# longest common subsequence

def lcs(X, Y):

    # base case
    for i in range(m+1):
        dp[i][0] = 0
    for j in range(n+1):
        dp[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            q = 0
            if X[i-1] == Y[j-1]:
                q = 1 + dp[i-1][j-1]
            else:
                q = max(dp[i-1][j], dp[i][j-1])
            dp[i][j] = q

    return dp[m][n]


if __name__=='__main__':
    str1 = input()
    str2 = input()
    m = len(str1)
    n = len(str2)
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    print(lcs(str1, str2))
    
