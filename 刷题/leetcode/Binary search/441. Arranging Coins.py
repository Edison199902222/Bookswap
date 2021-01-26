
'''
这道题需要转换一下 变成二分法
首先 怎么算第n行 从1 到 第n 行所有的 node呢 （n * n+1）//2
然后这就是一个二分发的问题了
直接找
最后先检查 是不是right 小于等于n 如果是 说明right 没有满足或者 right刚好满足
如果 right是大于n的话 说明我们要找的行是left
'''

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left + 1 < right:
            # 求和公式 首项 加 末项 乘项数 //2
            mid = left + (right - left)/2
            temp_mid = (mid * (mid + 1))//2
            if temp_mid == n:
                return mid
            elif temp_mid > n:
                right = mid
            elif temp_mid < n:
                left = mid
        if (right * (right + 1))/2 <= n:
            return right
        else:
            return left