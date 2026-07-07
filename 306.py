class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(1, n - i):
                if i > 1 and num[0] == '0':
                    break 
                if j > 1 and num[i] == '0':
                    break
                
                num1 = int(num[:i])
                num2 = int(num[i:i+j])
                k = i + j
                
                while k < n:
                    next_sum = num1 + num2
                    next_sum_str = str(next_sum)
                    
                    if not num[k:].startswith(next_sum_str):
                        break
                    
                    k += len(next_sum_str)
                    num1 = num2
                    num2 = next_sum
                
                if k == n:
                    return True
                    
        return False
