class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        jumps = 0
        far = 0
        curr = 0
        for i in range(n-1):
            far = max(far, i+nums[i])
            if i == curr:
                curr = far
                jumps += 1
                if curr >= n-1:
                    break
        return jumps
        
        