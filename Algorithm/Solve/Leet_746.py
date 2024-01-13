class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-2], dp[n-1])