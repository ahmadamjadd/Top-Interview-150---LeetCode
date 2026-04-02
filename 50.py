class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        def help(base, power):
            if power == 1:
                return base
            
            if power % 2 == 0:
                half = help(base, power // 2)
                return half * half
            else:
                half = help(base, (power - 1) // 2)
                return base * half * half

        finalAns = help(x, abs(n))

        if n < 0:
            return 1 / finalAns
        
        return finalAns
