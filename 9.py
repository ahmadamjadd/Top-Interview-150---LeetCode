class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        old_val = x
        new_val = 0
        while old_val > 0:
            digit = old_val % 10
            old_val = old_val // 10
            new_val = (new_val*10)+digit
        if x == new_val:
            return True
        return False

        
        
