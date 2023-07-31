class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = 1 + d.get(i, 0)
        s = set(d.values())
        return True if len(s) == len(d) else False
