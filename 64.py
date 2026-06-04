class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        memo = {}
        
        def help(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
                
            if i < 0 or j < 0:
                return float('inf')
                
            if i == 0 and j == 0:
                return grid[i][j]
            
            cost1 = help(i-1, j)
            cost2 = help(i, j-1)
            
            result = grid[i][j] + min(cost1, cost2)
            memo[(i, j)] = result
            
            return result
            
        return help(m - 1, n - 1)
