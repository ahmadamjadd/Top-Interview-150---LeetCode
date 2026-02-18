class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final_ans = []
        
        def backtrack(current_sum, path, start_index):
            if current_sum == target:
                final_ans.append(list(path))
                return
            
            if current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                path.append(candidate)
                backtrack(current_sum + candidate, path, i)
                path.pop()

        backtrack(0, [], 0)
        return final_ans
