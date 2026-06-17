import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap = [-count for count in task_count.values()]
        heapq.heapify(max_heap)
        
        cooldown_queue = deque()
        time = 0
        
        while max_heap or cooldown_queue:
            time += 1
            
            if max_heap:
                current_freq = heapq.heappop(max_heap) + 1
                
                if current_freq < 0:
                    cooldown_queue.append([current_freq, time + n])
                    
            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_task_freq = cooldown_queue.popleft()[0]
                heapq.heappush(max_heap, ready_task_freq)
                
        return time
