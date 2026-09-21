class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        res, count = 0, 0
        s, e = 0, 0
        
        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            
            res = max(res, count)
            
        return res
