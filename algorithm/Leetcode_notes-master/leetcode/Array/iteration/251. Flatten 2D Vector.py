class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.next_item = None
        self.v = v
        self.row, self.col = 0, -1

    def next(self):
        """
        :rtype: int
        """
        if self.next_item is None:
            self.hasNext()
        temp, self.next_item = self.next_item, None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.next_item is not None:
            return True
        self.col += 1
        while self.row < len(self.v) and self.col >= len(self.v[self.row]):
            self.row += 1
            self.col = 0
        if self.row < len(self.v) and self.col < len(self.v[self.row]):
            self.next_item = self.v[self.row][self.col]
            return True
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
'''
跟 lt 的528 套路一样
next item 指向我们即将要return的element
在next 函数中 每次调用has next 去用来移动next element
'''
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()