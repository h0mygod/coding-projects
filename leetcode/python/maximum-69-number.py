class Solution:
    def maximum69Number(self, num: int) -> int:
        for ind, i in enumerate(str(num)):
            if i == '6':
                return num + 3*(10**((len(str(num))-1)-ind))
            else:
                continue
        return num
