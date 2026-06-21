import heapq

class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        tails = {}
        
        for x in nums:
            if (x - 1) in tails and tails[x - 1]:
                shortest_length = heapq.heappop(tails[x - 1])
                
                if x not in tails:
                    tails[x] = []
                heapq.heappush(tails[x], shortest_length + 1)
                
            else:
                if x not in tails:
                    tails[x] = []
                heapq.heappush(tails[x], 1)
                
        for lengths in tails.values():
            for length in lengths:
                if length < 3:
                    return False
                    
        return True
