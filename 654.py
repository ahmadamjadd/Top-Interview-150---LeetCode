# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def help(nums):
            if not nums:
                return None
            root = TreeNode()
            max_val = max(nums)
            root.val = max_val
            i = nums.index(max_val)
            root.left = help(nums[:i])
            root.right = help(nums[i+1:])
            return root
        return help(nums)



        
