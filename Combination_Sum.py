from collections import Counter

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def is_valid(path):
            if sum(path) == target:
                return True
            return False
        
        def backtrack(index, path):
            if sum(path) > target:
                return
            if is_valid(path):
                
                results.append(list(path))
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        backtrack(0,[])
        return results

        
