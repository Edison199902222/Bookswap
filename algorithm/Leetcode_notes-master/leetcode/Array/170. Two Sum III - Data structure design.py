'''
两种方法
但第一种更快
因为不用每次find 都创建一个新的dic
'''

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.num = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.num:
            self.num[number] += 1
        else:
            self.num[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for number in self.num:
            sub_value = value - number
            if sub_value in self.num:
                if number == sub_value:
                    if self.num[number] > 1:
                        return True
                else:
                    return True
        return False


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.num = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.num.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(self.num)):
            if value - self.num[i] in dic:
                return True
            dic[self.num[i]] = i
        return False

