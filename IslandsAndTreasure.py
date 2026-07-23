from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distance = 1
        
        while q:
            for _ in range(len(q)):
                rt, ct = q.popleft()
                
                for rd, nd in directions:
                    nr = rt + rd
                    nc = ct + nd
                    
                    if (nr < 0 or nr >= rows or 
                        nc < 0 or nc >= cols or 
                        grid[nr][nc] != 2147483647):
                        continue
                    
                    grid[nr][nc] = distance
                    q.append((nr, nc))
            
            distance += 1
