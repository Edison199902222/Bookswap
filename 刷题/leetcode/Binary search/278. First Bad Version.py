# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
'''
这是一个模版
普通二分法 是在while之中 直接找出最优解
而这个模版 是找出 两个可能性 然后进行判断
'''
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left + 1 < right:
            mid = left + (right - left) / 2
            if isBadVersion(mid) == False:
                left = mid
            else:
                right = mid
        if isBadVersion(left) == True:
            return left
        return right
