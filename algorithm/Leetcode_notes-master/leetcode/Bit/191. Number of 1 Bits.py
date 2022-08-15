'''
任何数&任何数-1 就是消除最后一个1
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while (n != 0):
            res += 1
            n = n & (n - 1)
        return res


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            res += (n & 1)
            n >>= 1
        return res
'''
 n & 1 可以检查 一个数字的最后一位是不是1 如果是最低位是1 那么会变成1 不是的话 会变成0
 每次检查最低位是不是1 然后对n 进行右移动操作 一位一位的看
'''
