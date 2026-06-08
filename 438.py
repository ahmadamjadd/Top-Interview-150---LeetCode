from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ans = []
        size = len(p)
        
        p_count = Counter(p) 
        
        for i in range(0, len(s) - size + 1):
            substring = s[i:i+size]
            
            if Counter(substring) == p_count:
                ans.append(i)
                
        return ans
