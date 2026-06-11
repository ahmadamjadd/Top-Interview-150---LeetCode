class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        current_sum = 0
        for i in range(k):
            current_sum += abs(arr[i] - x)
        
        min_sum = current_sum
        index = 0
        
        for i in range(1, len(arr) - k + 1):
            outgoing_val = abs(arr[i - 1] - x)
            incoming_val = abs(arr[i + k - 1] - x)
            current_sum = current_sum - outgoing_val + incoming_val
            
            if current_sum < min_sum:
                min_sum = current_sum
                index = i
                
        return arr[index:index+k]
