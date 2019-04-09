'''we have only 3 operations:- /3,/2,-1
we want to find min no of steps to change a no to 1
'''

#this is a recursion method

'''
def reduceNo(n):
    if n==1:
        return 0
    q1=float('inf')
    q2=float('inf')
    q3=float('inf')

    if n%3==0:
        q1 = 1+reduceNo(n/3)
    if n%2==0:
        q2 = 1+reduceNo(n/2)
    q3 = 1+reduceNo(n-1)

    return min(q1,q2,q3)

if __name__=="__main__":
    n = int(input("write the no you want to reduce"))
    ans = reduceNo(n)
    print(ans)

'''

# following is a memoization(top down) method
'''
def reduceNo(n):
    if n==1:
        return 0

    if memo[n]!=-1:
        return memo[n]
    
    q1=float('inf')
    q2=float('inf')
    q3=float('inf')

    if n%3==0:
        q1 = 1+reduceNo(n//3)
    if n%2==0:
        q2 = 1+reduceNo(n//2)
    q3 = 1+reduceNo(n-1)

    memo[n]= min(q1,q2,q3)
    return memo[n]

if __name__=="__main__":
    n = int(input("write the no you want to reduce"))
    memo=[-1]*(n+1) #memo contains the no of steps required from n to 1
    ans = reduceNo(n)
    print(ans)
'''

# following is a dp(bottom up) method

def reduceNo_DP(n):
    dp[0]=dp[1]=0
    dp[2]=dp[3]=1

    for currNo in range(4, n+1):
        q1=q2=q3=float('inf')

        if currNo %3 == 0:
            q1 = 1+dp[currNo//3]

        if currNo %2 ==0:
            q2 = 1+dp[currNo//2]
        q3 = 1+dp[currNo-1]

        dp[currNo] = min(q1,q2,q3)

    return dp[n]

if __name__=="__main__":
    n = int(input("write the no you want to reduce"))
    dp = [-1]*(n+1)  # dp contains the no of steps required from n to 1
    ans = reduceNo_DP(n)
    print(ans)

