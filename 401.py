class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
            
        ans = []
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        
        def backtrack(idx, count, curr_hours, curr_mins):
            if curr_hours >= 12 or curr_mins >= 60:
                return
            
            if count == turnedOn:
                ans.append(f"{curr_hours}:{curr_mins:02d}")
                return
            
            for i in range(idx, len(leds)):
                if i < 4:
                    backtrack(i + 1, count + 1, curr_hours + leds[i], curr_mins)
                else:
                    backtrack(i + 1, count + 1, curr_hours, curr_mins + leds[i])
                    
        backtrack(0, 0, 0, 0)
        
        return ans
