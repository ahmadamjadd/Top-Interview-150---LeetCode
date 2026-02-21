# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if not root.left and not root.right:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            tmp = TreeNode()
            tmp = root.right
            root.right = root.left
            root.left = None
            tmp2 = root
            while tmp2.right != None:
                tmp2 = tmp2.right
            tmp2.right = tmp
            
        
        
