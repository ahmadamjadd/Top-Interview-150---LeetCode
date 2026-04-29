class Solution:
    def check(self, s: str) -> bool:
        tmpList = s.split(".")
        
        for i in range(len(tmpList)):
            if not tmpList[i]:
                return False
                
            if tmpList[i][0] == "0" and len(tmpList[i]) > 1:
                return False
            elif not tmpList[i].isalnum():
                return False
            elif int(tmpList[i]) < 0 or int(tmpList[i]) > 255:
                return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        def backtrack(stop, current_s, index):
            if stop == 0:
                if self.check(current_s):
                    ans.append(current_s)
                    return True
                return False
                
            for i in range(index, len(current_s)):
                new_s = current_s[:i] + "." + current_s[i:]
                all_ok = backtrack(stop - 1, new_s, i + 2)

        backtrack(3, s, 1)
        return ans
