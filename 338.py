class Solution:
    def countBits(self, n: int) -> List[int]:
        if n < 4:
            dp = [0,1,1,2]
            return dp[:n+1]
        dp = [0]*(n+1)
        dp[0] =0
        dp[1] = 1
        dp[2] = 1
        dp[3] = 2
        stop = 8
        for i in range(4, n+1):
            if i == stop:
                stop = stop * 2
            dp[i] = 1 + dp[i-(stop//2)]
        return dp
            


        
