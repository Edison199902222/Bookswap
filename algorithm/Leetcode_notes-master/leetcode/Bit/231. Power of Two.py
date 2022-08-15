'''
n & (n - 1) 意思是把二进制位伤的1
比如4 二进制是 100， 操作后变成 000
所以我们发现，任何2 的次方，都是二进制上只有一个1， 所以如果操作以后，一定会变成0
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n&(n-1) == 0) and n!=0:
            return True
        return False
