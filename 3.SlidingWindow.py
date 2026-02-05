from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        final_ans = []
        left = 0
        for i in range(len(s)):
            right = i
            if s[right] in s[left:right]:
                final_ans.append(s[left:right])
                while s[right] in s[left:right]:
                    left +=1
        final_ans.append(s[left:])
        ans = max(final_ans, key = len)
        return len(ans)





        
