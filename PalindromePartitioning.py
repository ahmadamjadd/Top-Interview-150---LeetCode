class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def help(j, i, path):
            if j == len(s):
                ans.append(path[:])
                return
            
            if i >= len(s):
                return
            
            current_str = s[j:i+1]
            if current_str == current_str[::-1]:
                path.append(current_str)
                help(i + 1, i + 1, path)
                path.pop()
                
            help(j, i + 1, path)
            
        help(0, 0, [])
        return ans
