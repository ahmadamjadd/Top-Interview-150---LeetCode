class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        right = len(height) - 1
        left = 0
        while right > left:
            ans = max(ans, ((right-left)*min(height[left], height[right])))
            if min(height[left], height[right]) == height[left]:
                left+=1
            else:
                right -=1
        return ans
        


        
