class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        # 有几种path 可以变成以i 作为结尾lis
        count = [1] * n
        # 以 i 作为结尾的lis 是多少
        dp = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    # 小于dp[i]是不行的！只有等于lis才能加
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        # 得到最长的长度
        max_length = max(dp)
        result = 0
        for i in range(n):
            if dp[i] == max_length:
                result += count[i]
        return result