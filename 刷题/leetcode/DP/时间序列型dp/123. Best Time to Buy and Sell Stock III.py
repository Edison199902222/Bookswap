class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 表示 此轮买入第一股时 max profit
        # 1 表示 此轮卖出第一股时 max profit
        # 2 表示 此轮买入第二股时 max profit
        # 3 表示 此轮卖出第二股时 max profit
        if not prices:
            return 0
        # 初始化为最小值时因为每一次我们需要取最大值，有可能为负数，初始化为0 的话，负数取不到
        dp = [[float("-inf")] * 4 for i in range(len(prices))]
        # 需要考虑初始化
        dp[0][0] = - prices[0]
        # 卖出时初始化为0
        dp[0][1] = 0
        # 初始化为0 
        dp[0][3] = 0
        n = len(prices)

        for i in range(1, len(prices)):
            # 依赖于前一轮买入第一股时max profit 或 当前买入第一股
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            # 买入第二股， 所以要减， 因为只能第一次卖掉了才能买第二次， 所以依赖于前一轮卖掉第一支股票
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])

        return max(dp[n - 1][1], dp[n - 1][3])


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        left_max_profit = [0] * len(prices)
        min_value = prices[0]
        max_profit = 0
        # 代表第i天 包括 i 之前 交易所得的最大profit
        for i in range(1, len(prices)):
            min_value = min(min_value, prices[i])
            max_profit = max(max_profit, prices[i] - min_value)
            left_max_profit[i] = max_profit

        max_value = prices[-1]
        right_profit = 0
        result = 0
        # left_max_profit[i] + right_profit 的原因是 因为当天卖了之后，还可以再买
        for i in range(len(prices) - 2, - 1, -1):
            max_value = max(max_value, prices[i])
            right_profit = max(right_profit, max_value - prices[i])
            result = max(result, left_max_profit[i] + right_profit)

        return result

