# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        check =True
        def help(root1, root2):
            nonlocal check
            if not check:
                return
            if not root1 and not root2:
                return
            if not root1 and root2:
                check = False
                return
            if not root2 and root1:
                check = False
                return
            if root1.val == root2.val:
                help(root1.left, root2.left)
                help(root1.right, root2.right)
            else:
                check = False
            return
        help(p, q)
        return check

        
