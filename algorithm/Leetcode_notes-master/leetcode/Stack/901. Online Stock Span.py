class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        res = 1
        while self.stack and price >= self.stack[-1][0]:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''
单调栈问题 
题目意思是找到每一天 前面之中 小于等于当前天的连续的天数
所以 我们利用一个单调栈
里面的顺序是从大到小
一旦遇到一个price 是大于等于我们的栈顶时
我们就需要更新res 把此时栈顶元素pop出来
然后新的res 就会等于 加上pop出来的元素的res
再把我们新的price 跟 res 放进去
'''