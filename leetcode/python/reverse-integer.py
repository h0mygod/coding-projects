class Solution:
    def reverse(self, x: int) -> int:
        a = str(abs(x))
        if x == 0 or int(a[::-1]) < -2**31 or int(a[::-1]) > 2**31-1:
            return 0
        elif x < 0:
            while x % 10 == 0:
                x = x/10
                a = a[:-1]
            return f"-{a[::-1]}"

        else:
            while x % 10 == 0:
                x = x/10
                a = a[:-1]
            return a[::-1]
