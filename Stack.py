class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # Stores indices of the bars
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            # When we encounter a shorter bar, resolve the taller bars in the stack
            while stack and heights[stack[-1]] > heights[i]:
                # The popped bar is the limiting height
                height = heights[stack.pop()]
                
                # If stack is empty, this height extends all the way back to index 0.
                # Otherwise, it extends back to the index currently at the top of the stack.
                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
            
            # Push the current index onto the stack
            stack.append(i)
            
        # Resolve any remaining bars in the stack that extend to the end of the array
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        return max_area
