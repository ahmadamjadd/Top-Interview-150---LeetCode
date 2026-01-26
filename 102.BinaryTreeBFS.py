from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = Queue()
        q.put(root)
        while not q.empty():
            level_size = q.qsize()
            ans2 = []
            for _ in range(level_size):
                node = q.get()
                ans2.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ans.append(ans2)
        return ans
        

                


        