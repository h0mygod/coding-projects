class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lo = 0
        hi = k
        temp_sum = max_sum = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            print(temp_sum)
            temp_sum += nums[i + k - 1] - nums[i - 1]
            max_sum = max(temp_sum, max_sum)
        return max_sum / k
