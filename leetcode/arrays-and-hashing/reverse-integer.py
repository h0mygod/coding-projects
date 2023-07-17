class Solution:
    def reverse(self, x: int) -> int:
        a = str(abs(x))
        if x == 0 or int(a[::-1]) < -2**31 or int(a[::-1]) > 2**31-1:
            return 0
        elif x < 0:
            return (-int(a[::-1]))
        else:
            return (int(a[::-1]))
