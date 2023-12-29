# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         tmp = nums
#         prev, cnt = 0, 0

#         for i in range(len(tmp)):
#             cnt += 1
            
#             if tmp[i] != prev:
#                 prev = tmp[i]
#                 cnt = 1
#             else:
#                 if cnt > 2:
#                     tmp[i] = "_"
            
#         nums[:] = [i for i in tmp if i != "_"]

#         return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums) - 2:
            if nums[i] == nums[i+2]:
                nums.pop(i)
            else:
                i += 1
        
        return len(nums)