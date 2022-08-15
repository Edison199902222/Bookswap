class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        m = len(costs[0])
        # dp[i][j] 表示 第i 个房子， 染色成 j 的话费
        dp = [[0] * m for i in range(n + 1)]
        for i in range(1, n + 1):
            # 用来追踪当前前一个房子， 染色的最小值跟次小值
            # 必须初始化为 -1，不能使用float 因为dp[float]会报错
            min1, min2 = -1, -1
            for k in range(m):
                if min1 == -1 or dp[i - 1][k] < dp[i - 1][min1]:
                    min2 = min1
                    min1 = k
                elif min2 == -1 or dp[i - 1][k] < dp[i - 1][min2]:
                    min2 = k
            for j in range(m):
                if j != min1:
                    dp[i][j] = dp[i - 1][min1] + costs[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][min2] + costs[i - 1][j]
        result = float("inf")
        for i in range(m):
            result = min(result, dp[n][i])
        return result
'''
我们 不关注前一个房子染的什么颜色
我们对于当前房子来说，只关心用前一个房子的最小值 跟 当前房子染当前颜色的花费 加在一起
所以 我们 每一次， 先求出前一个房子的最小值，跟次小值
求完之后 
 dp[i][j] = dp[i - 1][min1] + costs[i - 1][j]
  dp[i][j] = dp[i - 1][min2] + costs[i - 1][j]
'''


'''
用dfs + memo
'''
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        self.memo = {}
        n = len(costs)
        m = len(costs[0])
        cost = float("inf")
        for color in range(m):
            cost = min(cost, self.dfs(n - 1, color, costs))
        return cost
    def dfs(self, house_number, color, costs):
        if house_number == 0:
            return costs[house_number][color]
        if (house_number, color) in self.memo:
            return self.memo[(house_number, color)]
        n = len(costs)
        m = len(costs[0])
        cost = float("inf")
        for pre_color in range(m):
            if pre_color == color:
                continue
            cost = min(cost, self.dfs(house_number - 1, pre_color, costs))
        self.memo[(house_number, color)] = cost + costs[house_number][color]
        return cost + costs[house_number][color]