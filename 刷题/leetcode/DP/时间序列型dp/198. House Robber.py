'''
Dp
状态转移是：
每一次遇到房子有两个状态 一个是rob 一个是not rob
如果rob的话 那么之前的房子就不能rob 所以是rob = not_rob + i
如果不偷的话 那么取决于之前的最大值 因为不偷的话 之前的房子可以rob 或者不rob
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        not_rob = 0
        for i in nums:
            pre = max(rob,not_rob)
            rob = not_rob + i
            not_rob = pre
        return max(not_rob,rob)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [[0]* 2 for i in range(len(nums))]
        n = len(nums)
        # 0 为抢， 1 为我不抢
        dp[0][0] = nums[0]
        for i in range(1, len(nums)):
            # 如果这一轮我要抢的话，上一轮不能抢！
            dp[i][0] = dp[i - 1][1] + nums[i]
            # 如果不抢的话， 上一轮可以抢 也可以不抢
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])

        return max(dp[n - 1][0], dp[n - 1][1])