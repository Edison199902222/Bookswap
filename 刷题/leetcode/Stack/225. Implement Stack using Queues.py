'''

使用一个queue 来模拟
push 时，我们只需要每添加一个元素进去后
把这个元素左边 所有的元素 都一个一个放进他的后面 就是stack 正确的顺序了

'''


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque = collections.deque()
        self.size = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.deque.append(x)
        self.size += 1
        for i in range(self.size - 1):
            self.deque.append(self.deque.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        self.size -= 1
        return self.deque.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.deque[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.deque) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
if __name__ == '__main__':
    ss = MyStack()
    list = [0, 1, 2, 3, 4]
    for i in range(5):
        ss.push(list[i])
    print(list)
    for i in range(5):
        print(ss.pop(), ',', end = '')
