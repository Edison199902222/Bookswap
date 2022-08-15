class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = [[float("inf")] * (m + 1) for i in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for k in range(1, min(i, m) + 1):
                # 起始点最多能到index k，保证前面有k - 1 个元素 形成k - 1个区间
                sums = 0
                for j in range(i, k - 1, - 1):
                    # 算最后一个区间的sums
                    sums += nums[j - 1]
                    # 最后一个区间的值， 跟 之前区间的largest sum 取最小值
                    dp[i][k] = min(dp[i][k], max(dp[j - 1][k - 1], sums))
        return dp[n][m]
