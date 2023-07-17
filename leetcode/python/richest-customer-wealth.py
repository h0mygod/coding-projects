class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = []
        for i in range(len(accounts)):
            wealth.append(sum(accounts[i]))
        wealth.sort()
        return wealth[-1]
