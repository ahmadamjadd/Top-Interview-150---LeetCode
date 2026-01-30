from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        choice = True
        array = []
        n = len(board)
        
        for i in range(n):
            row = board[n - i - 1]
            if choice:
                for j in range(n):
                    array.append(row[j])
            else:
                for j in range(n - 1, -1, -1):
                    array.append(row[j])
            choice = not choice          

        def bfs(array):
            n = len(array)
            q = deque([(0, 0)]) 
            visited = {0}
            
            while q:
                curr_idx, moves = q.popleft()
                
                if curr_idx == n - 1:
                    return moves
                
                for i in range(1, 7):
                    next_idx = curr_idx + i
                    
                    if next_idx < n:
                        destination = array[next_idx] - 1 if array[next_idx] != -1 else next_idx
                        
                        if destination not in visited:
                            visited.add(destination)
                            q.append((destination, moves + 1))
            return -1

        return bfs(array)
