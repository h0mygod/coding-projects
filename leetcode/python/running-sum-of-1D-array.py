class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        add = 0
        for i in nums:
            add += i
            ans.append(add)
        return ans
