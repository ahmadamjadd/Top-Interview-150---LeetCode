class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        mem = {}
        rows = len(obstacleGrid) -1
        cols = len(obstacleGrid[0]) -1
        if obstacleGrid[0][0] == 1:
            return 0

        def help(grid, r,c):
            if (r,c) in mem:
                return mem[(r,c)]
            if r == 0 and c == 0 and grid[r][c] != 1:
                return 1
            if r == 0 and c == 1 and grid[r][c] != 1:
                return 1
            if r ==1 and c == 0 and grid[r][c] != 1:
                return 1
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c] == 1:
                return 0
            ans = (help(grid, r-1, c)
            + help(grid, r,c-1) 
            )
            mem[(r,c)] = ans
            return ans
        return help(obstacleGrid, rows, cols)
            

        
