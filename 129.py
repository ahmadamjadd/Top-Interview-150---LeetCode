# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        visited = set()
        summ = 0
        num = ""
        def dfs(node,  visited, num = ""):
            nonlocal summ
            if not node.left and not node.right:
                num+=str(node.val)
                summ+=int(num)
                return
            visited.add(node)
            num+=str(node.val)
            if node.left:
                dfs(node.left, visited, num)
            if node.right:
                dfs(node.right, visited, num)
            return 
        dfs(root, visited, num)
        return summ
            

        
