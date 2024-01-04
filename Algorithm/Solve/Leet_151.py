class Solution:
    def reverseWords(self, s: str) -> str:
        strs = s.strip().split()[::-1]
        ans = " ".join(strs)
        
        return ans