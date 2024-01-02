# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         dp = [0] * (len(prices))
#         target = prices[0]

#         for i in range(1, len(prices)):
#             if prices[i] < target:
#                 target = prices[i]
#             else:
#                 dp[i] = prices[i] - target

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        target = prices[0]

        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - target)
            target = min(target, prices[i])

        return profit