# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        array = []
        def help(root):
            if root:
                help(root.left)
                array.append(root.val)
                help(root.right)
        help(root)
        for i in range(len(array)-1):
            min_diff = min(min_diff, abs(array[i]-array[i+1]))
        return min_diff
        
