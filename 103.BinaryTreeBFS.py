from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        choice = True
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            level_size = len(q)
            ans2 = []
            for _ in range(level_size):
                node = q.popleft()
                ans2.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if choice:
                ans.append(ans2)
            else:
                ans2.reverse()
                ans.append(ans2)
            choice = not choice
        return ans
        

                


        