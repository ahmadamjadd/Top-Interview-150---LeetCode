import heapq
import math
class Solution:
    def distance(self,point):
        return math.sqrt((point[0])**2 + (point[1]**2))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        pq = []
        for point in points:
            dist = self.distance(point)
            heapq.heappush(pq, (dist, point))
        ans = []
        for i in range(k):
            dist, point = heapq.heappop(pq)
            ans.append(point)
        return ans

        
