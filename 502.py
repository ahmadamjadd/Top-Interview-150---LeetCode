import heapq

def heap_sort_projects(profits, capital):
    projects = sorted(zip(capital, profits))
    return projects

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        check_list = heap_sort_projects(profits, capital)
        
        n = len(check_list)
        i = 0
        available_profits_heap = []
        
        for _ in range(k):
            while i < n and check_list[i][0] <= w:
                heapq.heappush(available_profits_heap, -check_list[i][1])
                i += 1
            
            if available_profits_heap:
                w += -heapq.heappop(available_profits_heap)
            else:
                break
                
        return w
