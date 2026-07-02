class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= maxChoosableInteger:
            return True
        
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
            
        memo = {}
        
        def dfs(choices, remainder):
            if choices in memo:
                return memo[choices]
            
            if choices[-1] >= remainder:
                return True
            
            for i in range(len(choices)):
                next_choices = choices[:i] + choices[i+1:]
                
                if not dfs(next_choices, remainder - choices[i]):
                    memo[choices] = True
                    return True
                    
            memo[choices] = False
            return False
            
        initial_choices = tuple(range(1, maxChoosableInteger + 1))
        return dfs(initial_choices, desiredTotal)
