class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.queue = []
        self.dic = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        if len(self.queue) == 0:
            return - 1
        while self.queue and self.dic[self.queue[0]] >= 2:
            self.queue.pop(0)
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.queue.append(value)
        if value in self.dic:
            self.dic[value] += 1
        else:
            self.dic[value] = 1
'''
利用一个queue 跟 一个字典 去做
queue来储存 unique number 
dic 来储存 每一个number 出现了多少次
add 负责 更新 queue 跟字典
每次 调用 showfirstunique 函数 我们都需要 遍历queue 如果发现第一个元素 出现了超过一次 那么就要把它 移除掉
然后再检查下一个元素 直到头部元素 是unique的
'''
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)