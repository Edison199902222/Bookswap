'''
先判断这个list的长度 是否是偶数
如果是偶数 那么就不用操作
是奇数 就把0添加到list中

'''

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        if n % 2 == 0:
            res = []
        else:
            res = [0]
        for i in range(1, (n // 2) + 1):
            res.append(i)
            res.append(-i)
        return res
