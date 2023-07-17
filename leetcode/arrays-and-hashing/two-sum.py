class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length):
            print(i)
            selected = nums.pop()
            print(selected)
            for x in range(len(nums)):
                if selected + nums[x] == target:
                    return [length-1-i, x]
