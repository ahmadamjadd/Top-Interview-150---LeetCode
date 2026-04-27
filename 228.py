class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        ans = []
        left = 0
        right = 0
        num = nums[0]
        for i in range(1,len(nums)):
            if num+1 == nums[i]:
                right +=1
                num+=1
                if i == len(nums)-1:
                    tmp = str(nums[left]) + "->" + str(nums[right])
                    ans.append(tmp)
                    break
            else:
                if right == left:
                    ans.append(str(nums[i-1]))
                else:
                    tmp = str(nums[left]) + "->" + str(nums[right])
                    ans.append(tmp)
                num = nums[i]
                right = i
                left = i
                if i == len(nums)-1:
                    ans.append(str(nums[i]))
                    break
        return ans


        
