class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashMap = {}
        l = s.split()
        if len(l) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in hashMap:
                if hashMap[pattern[i]] != l[i]:
                    return False
            else:
                if l[i] in hashMap.values():
                    return False
                hashMap[pattern[i]] = l[i]
        return True
        
