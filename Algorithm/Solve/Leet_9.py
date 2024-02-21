class Solution:
    def isPalindrome(self, x: int) -> bool:
        toString = str(x)

        if toString == toString[::-1]:
            return True
        else:
            return False