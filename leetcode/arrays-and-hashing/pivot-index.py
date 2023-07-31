class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[0:])
        for ind, i in enumerate(nums):
            right_sum -= i
            if left_sum == right_sum:
                return ind
            else:
                left_sum += i
        return -1
