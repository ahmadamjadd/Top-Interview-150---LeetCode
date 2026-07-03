import math
class Solution:
    def numSquares(self, n: int) -> int:
        possible_choices = []
        i = 1
        while i * i <= n:
            possible_choices.append(i * i)
            i += 1
        
        m = len(possible_choices)
        dp = [[n + 1] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = 0
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j < possible_choices[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j - possible_choices[i-1]])
                    
        return dp[m][n]


