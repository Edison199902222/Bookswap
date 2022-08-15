class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.result = []
        self.dic = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.dic[val].add(len(self.result))
        self.result.append(val)

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        # 找到要remove value 的index
        index = self.dic[val].pop()
        # 找到数组中最后一个数
        last_item = self.result[-1]
        # 找到他的index
        index2 = len(self.result) - 1
        # 如果要移除的数， 就是数组中最后一个
        if index == index2:
            # 直接pop
            self.result.pop()
        # 如果不是
        else:
            # 交换最后 两个的位置
            self.result[index], self.result[-1] = self.result[-1], self.result[index]
            # 移除最后一个item 之前的index
            self.dic[last_item].remove(index2)
            # 把交换后新的index 加进来
            self.dic[last_item].add(index)
            # 移除最后一个元素 也就是我们想要移除的val
            self.result.pop()
        if len(self.dic[val]) == 0:
            del self.dic[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.result)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()