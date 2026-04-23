class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        if n < 2:
            return 1
        for i in range(2, n+1):
            tmpSum = 0
            for j in range(1, i+1):
                tmpSum += dp[j-1] * dp[i-j]
            dp[i] = tmpSum
        return dp[n]


