class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
            }
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in brackets:
                stack.append(brackets[i])
            else:
                if i not in stack:
                    return False
                if i == stack[-1]:
                    stack.pop()
        return True if len(stack) == 0 else False
