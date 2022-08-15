class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curmax = 0
        curmin = 0
        max_total = float("-inf")
        min_total = float("inf")
        sums = 0
        for i in A:
            curmax = max(curmax + i, i)
            curmin = min(curmin + i, i)
            max_total = max(max_total, curmax)
            min_total = min(min_total, curmin)
            sums += i
        return max(max_total, sums - min_total) if max_total > 0 else max_total
'''
我们的目的是 需要找到 这个数组中的 最大子数组和， 最小子数组和， 跟数组总和
如果这个数组 不全是负数的话， 我们只需要比较 这个数组中的最大子数组和 跟 我们数组总和 减去 最小子数组和 就能得到最大值
因为，数组总和 减去 最小子数组和的意思是 我们把数组中 某一段最小的数组和找到了，这一段有可能是负数， 我们只需要丢掉这一段 就能找到我们最大值了
如果这个数组全是负数的话 上面的操作就不行了，全是负数的情况下 应该找 数组中的某个最大值 
'''