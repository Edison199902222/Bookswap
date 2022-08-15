'''
运用两个stack
一个in 一个out
push的时候 push进去in
如果要pop或者peak的时候 我们就首先 判断
如果out里面不为空 则直接pop
如果为空 就把in里面的东西pop出 再push进out里
'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.out:
            return self.out.pop()
        elif not self.out:
            while self.input:
                self.out.append(self.input.pop())
            return self.out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.out:
            return self.out[-1]
        elif not self.out:
            while self.input:
                self.out.append(self.input.pop())
            return self.out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not self.input) and (not self.out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()