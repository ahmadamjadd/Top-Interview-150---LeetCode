from collections import deque

class Solution:
    def check(self, string1: str, string2: str) -> bool:
        ans = False
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                if ans:
                    return False
                ans = True
        return ans

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        count = 0
        q = deque([(startGene, count)]) 
        visited = set([startGene])
        
        while q:
            node, c = q.popleft()
            
            if node == endGene:
                return c
                
            for candidate in bank:
                if self.check(candidate, node) and candidate not in visited:
                    q.append((candidate, c + 1))
                    visited.add(candidate)
                    
        return -1
