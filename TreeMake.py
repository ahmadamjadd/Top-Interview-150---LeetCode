# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map to get the index of any value in O(1) time
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        pre_idx = 0

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            
            # Base case: no elements in this subtree
            if in_left > in_right:
                return None

            # Pick current preorder element as root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Root splits inorder list into left and right subtrees
            mid = inorder_map[root_val]

            # Build left and right subtrees
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)
