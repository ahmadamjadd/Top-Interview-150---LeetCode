from collections import Counter
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        ans = []
        active_chars = set()
        curr_len = 0
        
        for char in s:
            active_chars.add(char)
            count[char] -= 1
            curr_len += 1
            
            if count[char] == 0:
                active_chars.remove(char)
                
            if len(active_chars) == 0:
                ans.append(curr_len)
                curr_len = 0
                
        return ans
