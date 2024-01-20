class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, cnt = [], 0

        for i in s:
            if i == ")":
                cnt -= 1
            if cnt > 0:
                res.append(i)
            if i == "(":
                cnt += 1

        return "".join(res)