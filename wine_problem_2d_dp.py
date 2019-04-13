# test case: 5 wine bottles with foll prices
# 2 3 5 1 4
# for year 1 length is 5, year 2 len is 4, year 3 len is 3, year 4 len is 2 and year 5 len is 1

# recursion method
'''
count = 0
def maxProfit(arr, beg, end, year):
    global count
    count += 1
    if beg>end:
        return 0

    q1 = arr[beg]*year + maxProfit(arr, beg+1, end, year+1)  #sell from beginning
    q2 = arr[end]*year + maxProfit(arr, beg, end-1, year+1)  #sell from end
    ans = max(q1,q2)
    return(ans)


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int,input().split()))
    print(maxProfit(prices, 0, n-1, 1))
    print(count)
'''

# memoization method

#memo is a 2d array of nxn with initial values -1
#rows defines beginning and columns end
#entry in (2,5) indicates maxProfit from 2(beg) to 5(end)
'''
count = 0
def maxProfit(arr, beg, end, year):
    global count
    count += 1
    if beg>end:
        return 0

    if memo[beg][end] != -1:
        return memo[beg][end]
    
    q1 = arr[beg]*year + maxProfit(arr, beg+1, end, year+1)  #sell from beginning
    q2 = arr[end]*year + maxProfit(arr, beg, end-1, year+1)  #sell from end
    ans = max(q1,q2)
    memo[beg][end]=ans
    return(ans)


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int,input().split()))
    memo = [[-1 for _ in range(n)] for _ in range(n)]  
    print(maxProfit(prices, 0, n-1, 1))
    print(count)
'''


# dp (bottom up) method

# here dp is a 2d matrix where rows and columns represents wine bottles
# and the value represents maxProfit for row(beg) and column(end)

def maxProfit(arr, n):
    year = n

    # when year is 5 and length is 1

    for i in range(n):
        dp[i][i] = year*arr[i]

    # when length is >=2 i.e. year is <=4
    year = n-1
    for len in range(2,n+1):
        start = 0
        end = n-len
        while(start<=end):
            endwindow = start+len-1
            dp[start][endwindow] = max(arr[start]*year + dp[start+1][endwindow],
                                       arr[endwindow]*year + dp[start][endwindow-1])
            start += 1
        year -= 1

    for i in range(n):
        for j in range(n):
            print(str(dp[i][j]).rjust(3,' '),end=' ')
        print()

    return(dp[0][n-1])

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int,input().split()))
    dp = [[0 for _ in range(n)] for _ in range(n)]  
    print(maxProfit(prices, n))
