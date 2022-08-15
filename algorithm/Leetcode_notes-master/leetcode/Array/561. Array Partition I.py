'''
要让整个list得到最大值
肯定就是先排序
然后最小的在一起
第二小的两个 在一起
'''

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans

