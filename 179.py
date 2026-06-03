class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        n = len(str_nums)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                combo1 = str_nums[j] + str_nums[j+1]
                combo2 = str_nums[j+1] + str_nums[j]
                
                if combo2 > combo1:
                    str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]
        
        result = "".join(str_nums)
        
        if result[0] == "0":
            return "0"
            
        return result
