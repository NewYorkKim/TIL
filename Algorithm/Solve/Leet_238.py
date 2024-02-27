class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post = 1, 1
        result = [0] * n

        for i in range(n):
            result[i] = pre
            pre *= nums[i]

        for j in range(n-1, -1, -1):
            result[j] *= post
            post *= nums[j]

        return result