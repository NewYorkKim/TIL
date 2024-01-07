class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        comp = list(set(nums))
        
        if len(comp) == len(nums):
            return False
        else:
            return True