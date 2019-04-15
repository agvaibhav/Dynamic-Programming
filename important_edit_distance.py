# edit distance problem
# used in autocorrect words
# we can perform 3 operations:- insertion, deletion, replacement
# cost of each operation is 1
# we have to perform in min no of operations
# input string is written in vertical manner and output in horizontal
# we add an empty character at the starting of each string

def editDist(inp, out):
    m = len(inp)
    n = len(out)

    dp[0][0] = 0
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] +1
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            q1 = dp[i-1][j-1]  # replacement
            q2 = dp[i-1][j]    # deletion
            q3 = dp[i][j-1]     # insertion
            dp[i][j] = min(q1, q2, q3) + (inp[i-1]!=out[j-1])

    return dp[m][n]

    
if __name__=='__main__':
    inp = input()
    out = input()
    dp = [[-1 for _ in range(len(out)+1)] for _ in range(len(inp)+1)]
    print(editDist(inp, out))
