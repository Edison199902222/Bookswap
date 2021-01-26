'''
使用dp
min_prices 表示的是 到第i天 的最低价格
max——profit 表示的是到现在为止最大的收益，
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 1:
            return 0
        min_prices = prices[0]
        max_profit = 0
        for i in range(1,n):
            min_prices = min(min_prices,prices[i])
            max_profit = max(max_profit,prices[i]-min_prices)# 取最大值 到底是不动 还是卖出
        return max_profit

