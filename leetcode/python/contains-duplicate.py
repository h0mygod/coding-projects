class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums2 = set()
        for i in nums:
            if i in nums2:
                return True
            else:
                nums2.add(i)
        return False
