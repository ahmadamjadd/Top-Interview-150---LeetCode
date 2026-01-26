from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = Queue()
        q.put(root)
        while not q.empty():
            sum  = 0
            level_size = q.qsize()
            for _ in range(level_size):
                node = q.get()
                sum += node.val
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ans.append(sum/level_size)
        return ans
            

        