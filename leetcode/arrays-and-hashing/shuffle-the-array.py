class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        a = []
        print(nums[0])
        for i in range(n):
            a.append(nums[0+i])
            a.append(nums[-n+i])
        return a
