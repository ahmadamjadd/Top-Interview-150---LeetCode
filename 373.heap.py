import heapq as hp

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = {(0, 0)}
        ans = []
        
        for _ in range(k):
            if not min_heap:
                break
                
            current_sum, r, c = hp.heappop(min_heap)
            ans.append([nums1[r], nums2[c]])
            
            if r + 1 < len(nums1) and (r + 1, c) not in visited:
                hp.heappush(min_heap, (nums1[r + 1] + nums2[c], r + 1, c))
                visited.add((r + 1, c))
                
            if c + 1 < len(nums2) and (r, c + 1) not in visited:
                hp.heappush(min_heap, (nums1[r] + nums2[c + 1], r, c + 1))
                visited.add((r, c + 1))
                
        return ans
