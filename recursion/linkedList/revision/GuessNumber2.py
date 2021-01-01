class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] *(n+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(i-1,0,-1):
                cost = n*n
                if i-j == 1 or i-j == 2:
                    cost = i-1
                else:
                    for k in range(j+1,i):
                        cost = min(cost,k+max(dp[k-1][j],dp[i][k+1]))
                dp[i][j] = cost
        return dp[n][1]
      