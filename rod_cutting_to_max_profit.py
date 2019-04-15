# rod cutting
# we are given profit of each length of rod
# we have to max profit


# recursion method
'''

def maxProfit(arr, totalLen):
    if totalLen == 0:
        return 0

    best = 0

    for len in range(1, totalLen+1):
        netProfit = arr[len] + maxProfit(arr, totalLen-len)
        best = max(best, netProfit)

    return best

if __name__=='__main__':
    totalLen = int(input())
    priceOfEachLen = list(map(int,input().split()))
    priceOfEachLen.insert(0,0)

    print(maxProfit(priceOfEachLen, totalLen))
'''

# memoization method
'''

def maxProfit(arr, totalLen):
    if totalLen == 0:
        return 0

    if memo[totalLen] != -1:
        return memo[totalLen]
    
    best = 0

    for len in range(1, totalLen+1):
        netProfit = arr[len] + maxProfit(arr, totalLen-len)
        best = max(best, netProfit)

    memo[totalLen] = best
    return best

if __name__=='__main__':
    totalLen = int(input())
    priceOfEachLen = list(map(int,input().split()))
    priceOfEachLen.insert(0,0)

    memo = [-1]*(totalLen+1)

    print(maxProfit(priceOfEachLen, totalLen))
'''

# bottom up (dp) method


def maxProfit(arr, totalLen):
    for len in range(1, totalLen+1):
        best = 0
        for cut in range(1, len+1):
            best = max(best, arr[cut] + dp[len-cut])

        dp[len] = best

    return dp[totalLen]  
    
if __name__=='__main__':
    totalLen = int(input())
    priceOfEachLen = list(map(int,input().split()))
    priceOfEachLen.insert(0,0)

    dp = [0]*(totalLen+1)

    print(maxProfit(priceOfEachLen, totalLen))
