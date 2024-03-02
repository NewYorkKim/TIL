class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = sorted([num * num for num in nums])

        return answer