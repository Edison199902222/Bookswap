class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = [[0 for i in range(3)] for i in range(len(costs))]
        n = len(costs)
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        for i in range(1, len(costs)):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        r_total = 0
        g_total = 0
        b_total = 0
        for i in range(len(costs)):
            r_total, g_total, b_total = min(g_total, b_total) + costs[i][0], min(r_total, b_total) + costs[i][1], min(g_total, r_total) + costs[i][2]
        return min(r_total, g_total, b_total)
'''
dp[i][j]表示 第i个房子如果涂第j个颜色 所需要的最少的钱
所以 我们 会得到动态转移方程
对于每个房子 我们可选择三个颜色 
然后对于每个颜色 我们是由 之前的房子选取的除自己以外的颜色 的最小值 加上自己的颜色的花费

'''