class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        
        for i, n in enumerate(nums):
            if idx < i:
                return False
            idx = max(idx, i + n)
            
        return True