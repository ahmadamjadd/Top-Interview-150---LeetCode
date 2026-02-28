class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                if (num >> i) & 1:
                    bit_sum += 1
            
            bit = bit_sum % 3
            if i == 31 and bit:
                ans -= (1 << 31)
            else:
                ans |= (bit << i)
                
        return ans
