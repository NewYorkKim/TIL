class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        ans = ""
        flag = ""
        
        for i in range(len(s)):
            if s[i].isdigit():
                ans += s[i]
            else:
                if (len(ans) == 0) and (len(flag) == 0):
                    if (s[i] == "+") or (s[i] == "-"):
                        flag += s[i]
                    else:
                        break
                else:
                    break
        
        if ans == "":
            ans = 0
        else:
            if flag == "-":
                ans = int(ans) * (-1)
            else:
                ans = int(ans)
        
        if ans < (-2)**31:
            return (-2)**31
        elif ans > 2**31 -1:
            return 2**31 -1
        else:
            return ans