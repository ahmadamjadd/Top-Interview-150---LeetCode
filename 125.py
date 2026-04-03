class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = "".join(char.lower() for char in s if char.isalnum())
        right = len(s_cleaned) -1
        left = 0
        while left < right:
            if s_cleaned[left] != s_cleaned[right]:
                return False
            right -=1
            left +=1
        return True        
