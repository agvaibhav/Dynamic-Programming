# we are given 2 sequences and k
# we have to find the longest common sequence if we can change k no of values in first sequence

def k_lcs(i, j ,k):
    if i>=n or j>=m:
        return 0
    
    if dp[i][j][k] != -1:
        return dp[i][j][k]

    res = 0
    
    if a[i]==b[j]:
        res = 1+k_lcs(i+1,j+1,k)

    else:
        if k>0:
            res = 1+k_lcs(i+1, j+1, k-1)  # when we converted a char in a to match with b
        res = max(res, k_lcs(i+1, j, k))
        res = max(res, k_lcs(i, j+1, k))

    dp[i][j][k] = res
    return res


if __name__=='__main__':
    inp = list(map(int, input().split()))
    n = inp[0]
    m = inp[1]
    k = inp[2]
    a = input().split()
    b = input().split()
    dp = [[[-1 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    print(k_lcs(0,0,k))
