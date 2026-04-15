class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0
            
        g.sort()
        s.sort()
        
        ans = 0
        s_pointer = len(s) - 1
        g_pointer = len(g) - 1
        
        while g_pointer >= 0 and s_pointer >= 0:
            if g[g_pointer] <= s[s_pointer]:
                ans += 1
                s_pointer -= 1
            g_pointer -= 1
            
        return ans
