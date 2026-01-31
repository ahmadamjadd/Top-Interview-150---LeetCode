class Solution:

    mapNum = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        def backtrack(digits, num, ans):
            if num == len(digits):
                result.append(ans)
                return
            for letter in self.mapNum[digits[num]]:
                backtrack(digits, num+1, ans+letter)

        backtrack(digits, 0, "")
        return result


        


        
