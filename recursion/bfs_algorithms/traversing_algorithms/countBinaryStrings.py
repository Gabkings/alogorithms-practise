class Solution:
    '''
    Binary Strings with at most K Consecutive One - O(n * k)
    Given two non-negative integers N and K, return the number of binary strings of length N with at most K consecutive ones
    '''

    def countBinaryStrings(self, n: int, k: int) -> int:
        dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(k + 1):
                dp[i + 1][0] += dp[i][j]
                if j < k:
                    dp[i + 1][j + 1] += dp[i][j]
        result = 0
        for j in range(k + 1):
            result += dp[n][j]
        return result
