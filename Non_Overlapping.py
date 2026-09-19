class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 0
        intervals.sort(key = lambda x: x[1])
        ans = 0
        curr = 0
        nex = 1
        while True:
            if intervals[curr][1] > intervals[nex][0]:
                ans +=1
                curr = curr
                nex = nex + 1
            else:
                curr = nex
                nex = nex + 1
            if nex == len(intervals):
                return ans
        return ans

            

        
