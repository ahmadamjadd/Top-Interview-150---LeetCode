class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max1, max2, max3 = 0, 0, 0
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
                
            max1 = max(max1, t[0])
            max2 = max(max2, t[1])
            max3 = max(max3, t[2])
            
        return [max1, max2, max3] == target
