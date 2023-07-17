class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for ind, select in enumerate(nums):
            if select > 0:
                break
            if ind > 0 and select == nums[ind - 1]:
                continue
            left, right = ind + 1, len(nums) - 1
            while left < right:
                total = select + nums[left] + nums[right]
                if total == 0:
                    result.append([select, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
