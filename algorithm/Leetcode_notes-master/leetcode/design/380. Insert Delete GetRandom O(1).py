class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.data)
        self.data.append(val)
        return True

    # 利用交换尾元素，然后删除尾元素 让time 降为o1
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        # 获取最后一个元素
        last_item = self.data[-1]
        # 获取删除元素的index
        val_index = self.dic[val]
        # 把最后一个元素的index 改成要删除元素的index
        self.dic[last_item] = val_index
        # 把要删除元素 跟 最后一个元素交换
        self.data[val_index] = last_item
        self.data[-1] = val
        self.data.pop()
        self.dic.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()