# class Solution:
#     def maximumOddBinaryNumber(self, s: str) -> str:
#         n = len(s)
#         s = sorted(list(s), reverse=True)
#         ans = ""

#         while len(ans) != n:
#             tmp = s.pop(0)

#             if tmp == "0":
#                 s.append(tmp)
#             else:
#                 if s.count("1") == 0:
#                     ans += "".join(s) + tmp
#                 else:
#                     ans += tmp
        
#         return ans

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = s.count("1")

        ans = "1" * (n - 1) + "0" * (len(s) - n) + "1"
        
        return ans