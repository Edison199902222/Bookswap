'''
首位相连的dp 我们可以切掉第一个 进行一次dp求解
切掉最后一个 进行一次dp求解 两者取最大值就行
dp[i]表示 直到i座房子， 我目前偷的最大值
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        ans1 = self.house_rab(nums[1:])
        ans2 = self.house_rab(nums[:len(nums) -1])
        return max(ans1,ans2)

    def house_rab(self, nums):
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]