class Solution:
    def kidsWithCandies(self, candies: list[int],
                        extraCandies: int) -> list[bool]:
        ans = []
        for i in candies:
            ans.append(all(n <= i+extraCandies for n in candies))
        return ans
