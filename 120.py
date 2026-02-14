class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        mem = {}
        
        def help(row, index):
            if row == 0 and index == 0:
                return triangle[0][0]
            if row < 0 or index < 0 or index > row:
                return float("inf")
            if (row, index) in mem:
                return mem[(row, index)]
            
            res = triangle[row][index] + min(help(row - 1, index), help(row - 1, index - 1))
            mem[(row, index)] = res
            return res

        last_row = len(triangle) - 1
        return min(help(last_row, i) for i in range(len(triangle[last_row])))
