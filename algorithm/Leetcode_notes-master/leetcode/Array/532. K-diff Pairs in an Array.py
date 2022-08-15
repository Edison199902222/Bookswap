import collections

'''
先把数组中 出现的数字与出现的次数 统计
然后发现 如果差异大于0的话 并且 当前数字加上差异 在字典中 就说明存在这么一队
或者 如果差异等于0的话 只要自身的数字 出现一次以上 也算一组
'''
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = collections.Counter(nums)
        res = 0
        for i in counter:
            if (k > 0 and i + k in counter)  or ( k == 0 and counter[i] > 1):
                res += 1
        return res
