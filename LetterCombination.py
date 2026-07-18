class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        ans = []
        path = [] 
        
        def backtrack(index):
            if index == len(digits):
                ans.append("".join(path)) 
                return
            
            for choice in dic[digits[index]]:
                path.append(choice) 
                backtrack(index+1)
                path.pop() 
                
        backtrack(0)
        return ans
