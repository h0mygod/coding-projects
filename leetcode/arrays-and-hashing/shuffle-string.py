class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        dic = {}
        ans = ""
        cur = 0
        for n in indices:
            dic[n] = dic.get(n, s[cur])
            cur += 1
        for i in sorted(indices):
            ans += dic[i]
        return ans
