from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] 

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stack_ind = stack.pop()
                res[stack_ind] = i - stack_ind
            stack.append(i)
            
        return res
