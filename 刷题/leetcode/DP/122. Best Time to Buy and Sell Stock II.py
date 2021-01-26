

'''
可以用贪心算法 跟dp算
但是贪心算法局限性很大
用两种把 分别写
这道题用dp还是难以理解
'''
class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(len(prices)):
            if i < len(prices)-1 and prices[i+1] > prices[i]:
                profit+=prices[i+1] - prices[i]
        return profit

    def maxProfitOptimizedDP(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        sell = 0
        buy = -prices[0]
        for i in range(1,n):
            sell = max(sell,buy + prices[i]) # 选择继续保持不卖出 还是选择卖出
            buy = max(buy,sell - prices[i]) # 选择不买进 还是买进
        return sell

if __name__ == '__main__':
    solution = Solution()
    list = [1,2,3,4,5]
    print(solution.maxProfit(list))

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n < 2:
            return 0
        min_value = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            # 如果当前值大于前面的最小值，说明有利可图
            if prices[i] > min_value:
                max_profit += (prices[i] - min_value)
            # 每一次都把min value 更新成 当前数
            # 两种情况，一种情况当前数大于前面的最小值，那么前面已经用了，不能再使用 所以用当前price 更新
            # 第二种情况，当前数小于前面的数，那肯定最小值是当前的
            min_value = prices[i]
        return max_profit