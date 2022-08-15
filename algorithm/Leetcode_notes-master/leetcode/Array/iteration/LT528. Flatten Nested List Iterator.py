"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.next_item = None
        self.stack = []
        for num in reversed(nestedList):
            self.stack.append(num)

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        if self.next_item is None:   # 检查下一个是不是None，如果是None 我们就需要调用has next 函数来帮我们检查
            self.hasNext()
        temp, self.next_item = self.next_item, None
        return temp

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        if self.next_item is not None:
            return True

        while self.stack:   # 让self next item 指向下一个 element
            temp = self.stack.pop()
            if temp.isInteger():
                self.next_item = temp.getInteger()
                return True
            for element in reversed(temp.getList()):
                self.stack.append(element)

        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())