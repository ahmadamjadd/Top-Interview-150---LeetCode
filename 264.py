import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        min_heap = [1]
        seen = {1}
        prime_factors = [2, 3, 5]
        current_ugly = 1
        
        for _ in range(n):
            current_ugly = heapq.heappop(min_heap)
            
            for factor in prime_factors:
                new_ugly = current_ugly * factor
                
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(min_heap, new_ugly)
                    
        return current_ugly
