import collections

class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = [0] * len(nums)
        
        # for i in range(len(nums)):
        #     if i == 0:
        #         dp[i] = nums[i]
        #     elif i == 1:
        #         dp[i] = max(dp[i-1], nums[i])
        #     else:
        #         dp[i] = max(dp[i-1], dp[i-2] + nums[i])
                
        # return max(dp)

        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.defaultdict(int)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp.popitem()[1]