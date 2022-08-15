class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.max_stack) == 0:
            self.max_stack.append(x)
            return
        if self.max_stack[-1] > x:
            self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) != 0:
            self.max_stack.pop()
            return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        if len(self.max_stack) != 0:
            return self.max_stack[-1]

    def popMax(self):
        """
        :rtype: int
        """
        val = self.peekMax()
        buff = []
        while self.top() != val:
            buff.append(self.pop())
        self.pop()
        while len(buff) != 0:
            self.push(buff.pop())
        return val
'''
储存两个stack
一个是普通的
一个保留每一步的最大值的
push函数 每次同时把值压入两个stack
但是压入max_stack的时候需要 判断 如果目前的值大于max stack中的顶值 那么压入，
如果不是的话 压入之前的值 保证跟普通 stack 一样
pop 的时候 记着 两个stack 同时pop
pop max 
利用val 指向 最大值
然后创建新的一个 stack 
只要原stack 顶部元素 不等于最大值 我们就pop出来 从原stack中pop 出来的 都放进新stack中 暂时储存
然后再pop出最大值
把新stack中 的值 push进去
'''
    # Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()