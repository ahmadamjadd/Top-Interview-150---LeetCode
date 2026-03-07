class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_tmp = int(a,2)
        b_tmp = int(b,2)
        ans = a_tmp + b_tmp
        return bin(ans)[2:]
        
