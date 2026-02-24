class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_dict = {}
        for i in range(len(nums)):
            array_dict[nums[i]] = i
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in array_dict:
                if i == array_dict[tmp]:
                    continue
                return [i, array_dict[tmp]]
