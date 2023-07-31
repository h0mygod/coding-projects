class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        seen = 0
        for i in t:
            if seen != len(s) and i == s[seen]:
                seen += 1
        return True if seen == len(s) else False
