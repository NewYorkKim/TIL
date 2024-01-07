class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits))) + 1
        ans = list(map(int, list(str(num))))
        
        return ans