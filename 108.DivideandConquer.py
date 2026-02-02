# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def help(nums):
            if not nums:
                return None
            middle = len(nums)//2
            node = TreeNode()
            node.val = nums[middle]
            node.left = help(nums[0:middle])
            node.right = help(nums[middle+1: len(nums)])
            return node
        
        return help(nums)


