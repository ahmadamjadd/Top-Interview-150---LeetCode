class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # Initialize (n + 1) x (amount + 1) table with infinity
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

        # Base case: 0 coins needed to make amount 0
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(1, amount + 1):
                if coin > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coin])

        ans = dp[n][amount]
        return ans if ans != float('inf') else -1
