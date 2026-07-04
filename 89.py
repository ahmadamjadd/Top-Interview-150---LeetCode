class Solution:
    def check(self, num1: int, num2: int) -> bool:
        # XOR the numbers. If they differ by 1 bit, the result is a power of 2.
        x = num1 ^ num2
        return (x & (x - 1)) == 0 and x != 0

    def grayCode(self, n: int) -> List[int]:
        target_length = 2 ** n
        ans = [0]
        visited = {0} # O(1) lookup to fix the TLE

        def backtrack() -> bool:
            # Correct base case
            if len(ans) == target_length:
                return True
            
            for num in range(1, target_length):
                if num in visited:
                    continue
                
                if self.check(ans[-1], num):
                    # DO
                    ans.append(num)
                    visited.add(num)
                    
                    # RECURSE and check for early exit
                    if backtrack(): 
                        return True
                    
                    # UNDO (Backtrack)
                    ans.pop()
                    visited.remove(num)
                    
            return False

        backtrack()
        return ans
