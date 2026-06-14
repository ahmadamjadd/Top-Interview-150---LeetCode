class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] +=1
        for key, value in hashmap.items():
            if value > len(nums)//3:
                ans.append(key)
        return ans

        
