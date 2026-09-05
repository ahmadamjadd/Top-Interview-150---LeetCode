class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                insert_op = dfs(i, j + 1)
                delete_op = dfs(i + 1, j)
                replace_op = dfs(i + 1, j + 1)
                
                memo[(i, j)] = 1 + min(insert_op, delete_op, replace_op)
                
            return memo[(i, j)]
        
        return dfs(0, 0)
