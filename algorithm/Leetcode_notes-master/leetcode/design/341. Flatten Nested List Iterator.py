class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.next_item = None
        for ele in reversed(nestedList):
            self.stack.append(ele)

    def next(self) -> int:
        if self.next_item is None:
            self.hasNext()
        temp, self.next_item = self.next_item, None
        return temp

    def hasNext(self) -> bool:
        if self.next_item is not None:
            return True
        while self.stack:
            element = self.stack.pop()
            if element.isInteger():
                self.next_item = element.getInteger()
                return True
            else:
                for ele in reversed(element.getList()):
                    self.stack.append(ele)
        return False
'''
利用stack 储存之前的东西
'''