class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a = 0
        for i in jewels:
            a += stones.count(i)
        return a
