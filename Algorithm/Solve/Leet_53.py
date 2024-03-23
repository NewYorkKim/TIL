class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ans = float('-inf')
        # cur = 0

        # for num in nums:
        #     cur += num

        #     if cur > ans:
        #         ans = cur

        #     if cur < 0:
        #         cur = 0
        
        # return ans

        sums = [nums[0]]

        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))

        return max(sums)