class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                val2, val1 = int(stack.pop()), int(stack.pop())
                stack.append(val1 + val2)
            elif i == "*":
                val2, val1 = int(stack.pop()), int(stack.pop())
                stack.append(val1 * val2)
            elif i == "-":
                val2, val1 = int(stack.pop()), int(stack.pop())
                stack.append(val1 - val2)
            elif i == "/":
                val2, val1 = int(stack.pop()), int(stack.pop())
                stack.append(val1 / val2)
            else:
                stack.append(i)
        return int(stack[0])
