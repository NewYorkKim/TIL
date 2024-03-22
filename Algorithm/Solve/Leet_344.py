class Solution:
    def reverseString(self, s: List[str]) -> None:
        # s[:] = s[::-1]
        s.reverse()