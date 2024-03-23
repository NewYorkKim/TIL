import collections

class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        # dp = [0] * (n + 2)
        # dp[1] = 1
        # dp[2] = 2
        
        # if n <= 2:
        #     return dp[n]
        
        # for i in range(3, n+1):
        #     dp[i] = dp[i-2] + dp[i-1]

        # return dp[n]

        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.dp[n]