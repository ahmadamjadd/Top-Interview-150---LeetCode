class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        k = 1
        while 5**k <= n:
            ans += (n//(5**k))
            k+=1
        return ans

