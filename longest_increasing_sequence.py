# longest increasing subsequence
# we are given some numbers we have to find the longest sequence which is increasing or non decreasing
# we will initialise the values of each number by 1
# if a no j that appears before a no i is smaller than i that means j can be absorbed by i
# we will increase the value of i if j<i can be absorbed by i and the final value of a no is max of all possible values


def lis(arr, n):
    # base case
    dp = [1] * n

    
    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<=arr[i]:
                curLen = 1+dp[j]
                dp[i] = max(curLen, dp[i])

    print(dp)
    return max(dp)    


if __name__=='__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(lis(arr,n))
