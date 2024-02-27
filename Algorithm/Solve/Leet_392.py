class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        cnt = 0

        for i in range(m):
            if len(s) == 0:
                break
            else:
                if s[0] == t[i]:
                    s = s[1:]
                    cnt += 1
        
        if cnt == n:
            return True
        else:
            return False