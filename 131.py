class Solution:
    def partition(self, s: str) -> list[list[str]]:
        memo = {}

        def solve(substring):
            if not substring:
                return [[]]
            if substring in memo:
                return memo[substring]
            
            res = []
            for i in range(1, len(substring) + 1):
                prefix = substring[:i]
                if prefix == prefix[::-1]:
                    suffixes = solve(substring[i:])
                    for suf in suffixes:
                        res.append([prefix] + suf)
            
            memo[substring] = res
            return res

        return solve(s)
