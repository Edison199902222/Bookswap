'''
这道题是有规律的
规律就是 两个数 如果 %k 后的余数相同
那么他们两个的差 肯定是k的倍数
0 是一个特殊case
所以 我们初始化 字典的时候 我们需要先把 0 放进去
然后遍历数组 每次先检查 k 是不是0 不是0 才可以除余
每次把 当前数字 除余 后 放进字典里 如果除余后的数字 已经在字典中 看看 两个数字的index 是不是超过1 如果超过1 直接return
'''

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        sums = 0
        dic[0] = -1
        for i in range(len(nums)):
            sums += nums[i]
            if k != 0:
                sums %= k
            if sums in dic:
                if i - dic[sums] > 1:
                    return True
            else:
                dic[sums] = i
        return False