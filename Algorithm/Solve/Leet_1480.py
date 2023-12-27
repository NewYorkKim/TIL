class Solution(object):
    def runningSum(self, nums):
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]

        return dp