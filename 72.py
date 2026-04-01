class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        
        def help(w1, w2):
            if (w1, w2) in mem:
                return mem[(w1, w2)]
            
            if not w1:
                return len(w2)
            if not w2:
                return len(w1)
            
            if w1[-1] == w2[-1]:
                ans = help(w1[:-1], w2[:-1]) 
            else:
                path1 = help(w1[:-1], w2[:-1]) + 1 
                path2 = help(w1, w2[:-1]) + 1      
                path3 = help(w1[:-1], w2) + 1      
                ans = min(path1, path2, path3)
            
            mem[(w1, w2)] = ans
            return ans
        
        return help(word1, word2)
