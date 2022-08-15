
'''
用循环 每次首先检查 当前的数是不是 个位数
然后 创建一个temp 用来得到 当前数字操作过后的数
每次temp 加上num 的最右边的位 （ % 10 代表得到最右边的数）
然后num 再去掉最右边的数
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if 0 <= num <= 9:
            return num
        while num:
            if 0 <= num <= 9:
                return num
            temp = 0
            while num:
                temp += num % 10
                num //= 10
            num = temp


