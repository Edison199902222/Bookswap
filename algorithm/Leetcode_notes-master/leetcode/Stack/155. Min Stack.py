class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        创建两个stack 一个记录最小值 从大到小
        一个记录所有的push进来的元素
        """
        self.A = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        如果stack A中没有元素
        那么push进来的x 肯定就是目前最小元素
        同时加进min 跟 A中
        以后只有小于 min 最后一个元素的 元素 才可 进min
        """
        A = len(self.A)
        if A == 0:
            self.min_stack.append(x)
        else:
            last_element = self.min_stack[-1]
            if last_element >= x:
                self.min_stack.append(x)
        self.A.append(x)

    def pop(self):
        """
        :rtype: None
        如果A大于0 并且pop出来的元素正好跟min里的最小元素相等
        那么同时pop出去
        """
        if len(self.A) > 0 and self.A.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
