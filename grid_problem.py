#Grid problem
# to find the min cost of travelling from 1 point to another

def minCost(grid, row, col):
    dp = [[-1 for _ in range(col)] for _ in range(row)]

    #base case
    dp[0][0] = grid[0][0]

    # fill the first row
    for c in range(1,col):
        dp[0][c] = dp[0][c-1] + grid[0][c]

    # fill the first col
    for r in range(1,row):
        dp[r][0] = dp[r-1][0] + grid[r][0]

    # fill remaining cells
    for r in range(1,row):
        for c in range(1,col):
            dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]

    return dp[row-1][col-1]



if __name__=='__main__':
    grid =[[1,2,3],[4,8,2],[1,5,3]]
    ans = minCost(grid, 3, 3)
    print(ans)
