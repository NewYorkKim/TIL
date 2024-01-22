class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = [0] * (n + 1)
        ans1, ans2 = 0, 0

        for num in nums:
            cnt[num] += 1

        for i in range(1, n+1):
            if cnt[i] > 1:
                ans1 = i
            if cnt[i] == 0:
                ans2 = i
            
        return [ans1, ans2]