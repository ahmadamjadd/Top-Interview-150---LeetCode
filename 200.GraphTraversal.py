class Solution:
    def dfs(self, grid: List[List[str]], r, c):
        if r < 0 or r >= len(grid) or c <0 or c >= len(grid[0]) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num+=1
                    self.dfs(grid, i, j)
        return num
