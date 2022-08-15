'''
先得到左边累乘的结果 然后再乘以右边累乘的结果 就会得到最后的结果
要注意的是 首先 list第一个 左边乘积要设置为1因为 第一个元素左边没有乘积
乘右边乘积时 设置一个right 初始化为1 因为数组最后一个数字的右边是没有乘积的
 去跟踪 第i个 右边的累计和
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:return []
        res = [0 for i in range(len(nums))]
        res[0] = 1
        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*right
            right = right * nums[i]
        return res