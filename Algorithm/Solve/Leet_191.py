class Solution:
    def hammingWeight(self, n: int) -> int:
        n = format(n, 'b')
        cnt = n.count("1")

        return cnt