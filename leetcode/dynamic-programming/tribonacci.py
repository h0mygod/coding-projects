class Solution:
    def tribonacci(self, n: int) -> int:
        res = collections.deque([0, 1, 1])
        if n<3:
            return res[n]
        else:
            for i in range(3, n):
                res.append(sum(res))
                res.popleft()
            return sum(res)
