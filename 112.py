# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.ans = False
        sum = 0
        def help(root, sum):
            if self.ans:
                return
            sum += root.val
            if not root.left and not root.right:
                if targetSum == sum:
                    self.ans = True
            if root.left:
                help(root.left, sum)
            if root.right:
                help(root.right, sum)
        help(root, sum)
        return self.ans


        
