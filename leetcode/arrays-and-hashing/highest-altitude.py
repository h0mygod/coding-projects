class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = curr_sum = 0
        for i in gain:
            curr_sum += i
            highest = max(highest, curr_sum)
        return highest
