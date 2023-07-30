class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        s = " ".join(s[::-1])
        return s
