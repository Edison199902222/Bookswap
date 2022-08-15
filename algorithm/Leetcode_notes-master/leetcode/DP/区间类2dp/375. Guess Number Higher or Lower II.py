class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i][j] 最少付多少钱保证猜中i 到 j 数字中的数字， 初始化n + 2 防止后面越界
        dp = [[0] * (n + 2) for i in range(n + 2)]

        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                # 找到我们要猜的数字
                # 要设置min cost, 去找 猜哪一个数字的时候，cost最小
                min_cost = float('inf')
                j = i + length - 1
                for k in range(i, j + 1):
                    # 选中要猜的数字后，需要在前后取最大值， 因为不一定是比我们猜的k大还是小，所以为了稳妥 需要取最大值
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    min_cost = min(min_cost, cost)
                dp[i][j] = min_cost
        return dp[1][n]


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        self.memo = {}
        return self.dfs(1, n)

    # 博弈类/区间dp， dp[i][j]表示从start 到 end 中 最少能保证win 的cost
    def dfs(self, start, end):
        if start >= end:
            return 0
        if (start, end) in self.memo:
            return self.memo[(start, end)]
        result = float("inf")
        # 从start 到end 中选择
        for k in range(start, end + 1):
            result = min(result, k + max(self.dfs(start, k - 1), self.dfs(k + 1, end)))
        self.memo[(start, end)] = result
        return result