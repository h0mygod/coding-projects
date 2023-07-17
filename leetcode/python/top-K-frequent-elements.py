class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        maxes = []
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)
        values = list(counts.values())
        keys = list(counts.keys())
        print(values)
        print(keys)
        for i in range(k):
            print(values.index(max(values)))
            temp = keys.pop(values.index(max(values)))
            values.pop(values.index(max(values)))
            maxes.append(temp)
        return maxes
