class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.memo = {}
        result = self.dfs(m, 0, target, houses, cost, n)
        return result if result != float("inf") else -1

    # dp[i][j][k] 表示还有i个 房子，j 表示前一个房子的颜色， k表示number of remaining unassigned neighborhoods
    def dfs(self, i, j, k, houses, cost, n):
        # 还有k个邻居需要分配，如果当前剩余邻居数量 大于我们剩下的房子数量 证明分配不了了
        if k < 0 or k > i:
            return float("inf")
        if i <= 0:
            return 0 if k == 0 else float("inf")
        if (i, j, k) in self.memo:
            return self.memo[(i, j, k)]
        result = float("inf")
        if houses[i - 1]:
            # 已被涂色过
            if houses[i - 1] != j:
                # 如果跟前一个房子的颜色不一样，那么多了一个邻居的set
                # 不能够使用k -= 1 因为k 改变了之后， 之后memo记录的k 也会改变
                result = self.dfs(i - 1, houses[i - 1], k - 1, houses, cost, n)
            else:
                result = self.dfs(i - 1, houses[i - 1], k, houses, cost, n)
        else:
            for color in range(1, n + 1):
                # 如果跟前一个房子的颜色不一样，那么多了一个邻居的set
                if color != j:
                    result = min(result, cost[i - 1][color - 1] + self.dfs(i - 1, color, k - 1, houses, cost, n))
                else:
                    result = min(result, cost[i - 1][color - 1] + self.dfs(i - 1, color, k, houses, cost, n))
        self.memo[(i, j, k)] = result
        return result
