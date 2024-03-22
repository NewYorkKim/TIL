import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = re.sub(r"[^a-z0-9]", "", s.lower())
        
        # if strs == strs[::-1]:
        #     return True
        # else:
        #     return False
        return s == s[::-1]