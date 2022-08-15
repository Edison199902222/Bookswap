class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k > n // 2:
            profit = 0
            for i in range(1, n):
                difference = prices[i] - prices[i - 1]
                if difference > 0:
                    profit += difference
            return profit
        # 表示当前持有股票，最多操作k 次，前i 个元素的最大值
        buy = [[float("-inf")] * (k + 1) for i in range(n + 1)]
        # 表示当时准备未股票， 最多操作k 次，前i个元素的最大值
        sell = [[float("-inf")] * (k + 1) for i in range(n + 1)]
        buy[0][0] = 0
        sell[0][0] = 0
        for i in range(1, n + 1):
            buy[i][0] = 0
            sell[i][0] = 0
            for j in range(1, k + 1):
                # 当前持有股票状态，可以由前面已经持有的状态 操作j次 + 什么都不做 转移来
                # 也可以 由前面未持有股票的状态 操作j 次 + 买当前的股票转移来
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i - 1])
                # 当前未持有股票状态， 可以由前面未持有的状态，操作j 次 + 什么都不做 转移来
                # 也可以由 前面已持有股票 j 次的状态 + 以当前price 卖掉股票 转移来 （ 卖掉股票不算进行一次操作）
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i - 1])
        return max(sell[n])