class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = str(s.lower())
        for x in s:
            if not x.isalnum():
                s = s.replace(x, '')
        n = -1
        for i in range(len(s)/2):
            if s[i] != s[n]:
                return False
            n -= 1
        return True
