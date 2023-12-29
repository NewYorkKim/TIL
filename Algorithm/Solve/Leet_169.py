from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = sorted(cnt.items(), key=lambda x: -x[1])[0][0]

        return ans