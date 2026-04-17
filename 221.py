class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for m in range(row):
            for n in range(col):
                if (m-1) < 0 or (n-1) <0:
                    dp[m][n] = int(matrix[m][n])
                    if ans < dp[m][n]:
                        ans = dp[m][n]
                else:
                    if matrix[m][n] == "1":
                        dp[m][n] = min(dp[m][n-1], dp[m-1][n], dp[m-1][n-1]) +1
                        if ans < dp[m][n]:
                            ans = dp[m][n]
                    else:
                        dp[m][n] = 0
        return ans**2
                    
        
