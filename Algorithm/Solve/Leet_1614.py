class Solution:
    def maxDepth(self, s: str) -> int:
        res, ans = [], 0
        tmp = 0

        for i in s:
            if i == ")":
                tmp -= 1
            if i == "(":
                tmp += 1
                ans = max(tmp, ans)

        return ans