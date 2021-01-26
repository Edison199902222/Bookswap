class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        # 限制最大能走到哪， 确定边界
        lenth = min(steps, arrLen)
        # dp[i][j] 意思是走到i，需要的步数
        self.memo = {}
        # 我们走到cur index, 剩余步数为steps的时候，可以产生出的valid的结果有多少种
        return self.dfs(0, steps, lenth, mod) % mod

    def dfs(self, cur, steps, lenth, mod):
        if (cur, steps) in self.memo:
            return self.memo[(cur, steps)]
        if cur >= lenth or cur < 0:
            return 0
        if cur != 0 and steps == 0:
            return 0
        if cur == 0 and steps == 0:
            return 1
        result = 0
        result += self.dfs(cur + 1, steps - 1, lenth, mod) % mod + self.dfs(cur - 1, steps - 1, lenth,
                                                                            mod) % mod + self.dfs(cur, steps - 1, lenth,
                                                                                                  mod) % mod
        self.memo[(cur, steps)] = result
        return result

