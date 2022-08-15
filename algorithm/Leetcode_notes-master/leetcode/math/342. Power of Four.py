class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1
'''
如果是 0 就直接 return FALSE
然后判断 除余4 是不是0 如果是的话 那么我们就可以除
当发现如果不是的时候 去检查 最后的num 是不是1 如果是1 那么说明 这个就是由4 相乘得到的 如果不是 就return false
'''