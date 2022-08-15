class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)
'''
dp[i]表示 从数组开头 到第i 个index 的最大sum是多少
index 0 当然是 自己本身了 因为前面没有数字
所以我们从数字 第1 个开始遍历 
dp 的 第i个index 取决于 之前的最大sum 加上自己 是不是 比自己本身大 
如果比自己本身小 那么我们没有必要加上前面的 
所以 用max
'''