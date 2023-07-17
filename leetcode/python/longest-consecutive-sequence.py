class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        longest = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                longest = max(longest, y - x)
        return longest
