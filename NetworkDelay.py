import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        min_heap = [(0, k)]
        visited = set()
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            if node in visited:
                continue
                
            visited.add(node)
            
            if len(visited) == n:
                return time
                
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))
                    
        return -1
