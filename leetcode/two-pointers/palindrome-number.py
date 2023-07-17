class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        a = str(x)

        if int(a) == int(a[::-1]):
            return True
        else:
            return False
