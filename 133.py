from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        q = deque([node])
        clones = {node: Node(node.val)}
        
        while q:
            current = q.popleft()
            
            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                clones[current].neighbors.append(clones[neighbor])
                
        return clones[node]
