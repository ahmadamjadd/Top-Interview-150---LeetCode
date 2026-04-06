class Solution:
    def check(self, board, i, j, m, n):
        count = 0
        if j+1 < n: 
            if board[i][j+1] == 1 or board[i][j+1] == 2:
                count +=1
        if j-1 >= 0:
            if board[i][j-1] == 1 or board[i][j-1] == 2:
                count +=1
        if i+1 < m:
            if board[i+1][j] == 1 or board[i+1][j] == 2:
                count +=1
        if i-1 >=0:
            if board[i-1][j] == 1 or board[i-1][j] == 2:
                count +=1
        if i+1 < m and j+1<n:
            if board[i+1][j+1] == 1 or board[i+1][j+1] == 2:
                count +=1
        if i-1 >= 0 and j-1 >=0:
            if board[i-1][j-1] == 1 or board[i-1][j-1] == 2:
                count +=1
        if i-1 >=0 and j+1 <n:
            if board[i-1][j+1] == 1 or board[i-1][j+1] == 2:
                count +=1
        if i+1 <m and j-1>=0:
            if board[i+1][j-1] == 1 or board[i+1][j-1] == 2:
                count +=1
        if count <2 or count >3:
            if board[i][j] == 1:
                board[i][j] = 2
        if count ==3 and board[i][j] == 0:
            board[i][j] = 3

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                self.check(board, i, j, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] ==2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1

        
