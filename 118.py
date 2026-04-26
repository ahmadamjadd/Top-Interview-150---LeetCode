class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        
        for i in range(1, numRows):
            row = [1]
            prev_row = res[i - 1]
            
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            
            row.append(1)
            res.append(row)
            
        return res
