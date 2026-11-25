from collections import deque
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                
                # The last node popped in this level is the rightmost node
                if i == level_len - 1:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return res
