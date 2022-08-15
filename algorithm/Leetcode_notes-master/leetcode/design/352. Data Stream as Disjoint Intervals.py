class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.result = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        # 有序插入
        bisect.insort_left(self.result, val)

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        result = []
        first = None
        # 输出列表，first 代表起点，如果发现当前num 跟前一个num 的差大于1，说明要添加一个区间
        for i in range(len(self.result)):
            if i == 0:
                first = self.result[i]
            else:
                if self.result[i] - self.result[i - 1] > 1:
                    result.append([first, self.result[i - 1]])
                    first = self.result[i]
        # 最后一个也要添加
        result.append([first, self.result[-1]])
        return result

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()