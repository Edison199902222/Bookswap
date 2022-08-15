class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(cost) + 1)]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp_1 = 0
        dp_2 = 0
        for i in range(2, len(cost) + 1):
            dp = min(dp_1 + cost[i - 2], dp_2 + cost[i - 1])
            dp_1 = dp_2
            dp_2 = dp
        return dp_2
'''
动态规划
先用一位数组
dp[i]代表 到第i个台阶 所需要最小的cost
然后 每一级台阶 取决于 前一个台阶的cost 加上到前台阶最小的cost 或者 前前台阶的cost 加上 到前前台阶最小的cost
最后return dp[n]就可以了
'''