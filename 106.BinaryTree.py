# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.index = len(postorder) -1 
        def helper(leftptr, rightptr):
            if rightptr <leftptr:
                return None
            root_val = postorder[self.index]
            root = TreeNode(val = root_val)
            self.index -=1
            mid_index = inorder_map[root_val]
            root.right = helper(mid_index + 1, rightptr)
            root.left = helper(leftptr, mid_index - 1)
            return root
        return helper(0, len(postorder) - 1)

        