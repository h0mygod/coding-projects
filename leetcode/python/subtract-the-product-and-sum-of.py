class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        adds = 0
        for i in str(n):
            prod *= int(i)
            adds += int(i)
        return prod-adds
