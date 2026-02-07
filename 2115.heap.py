import heapq as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            hp.heappush(max_heap, num*(-1))
        for _ in range(k-1):
            heappop(max_heap)
        return heappop(max_heap)*(-1)
        
