import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/k)
            return hours
        def bs():
            best = max(piles)
            high = max(piles)
            low = 1
            while high > low:
                mid = low + (high - low)//2
                hours = check(mid)
                if hours <= h:
                    best = mid
                    high = mid
                else:
                    low = mid+1
            return best
        return bs()



        
