class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            tmp = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                tmp *= nums[j]
            ans.append(tmp)
        
        return ans