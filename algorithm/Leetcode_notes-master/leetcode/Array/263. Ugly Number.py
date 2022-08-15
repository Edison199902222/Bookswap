'''
原理就是 如果发现 当前数字 可以把 某个factot 除余后 可以 ==0 说明可以相除 那么就除
如果发现 == 1的话 说明成功了 如果到最后 不可以的话 说明 false
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        factor = [2,3,5]
        for i in factor:
            while num % i == 0:
                num /= i
            if num == 1:
                return True
        return False