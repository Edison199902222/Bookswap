class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if len(jobDifficulty) < d:
            return - 1
        m = len(jobDifficulty)
        # dp[i][k] 前i个任务，分成k天的minimum difficulty of a job schedul
        dp = [[float("inf")] * (d + 1) for i in range(m + 1)]
        dp[0][0] = 0

        for i in range(1, m + 1):
            # 维护当前i元素 最多能分成几天做
            for k in range(1, min(i, d) + 1):
                # 找最后一天的开始任务j
                max_diff = float("-inf")
                for j in range(i, k - 1, -1):
                    max_diff = max(max_diff, jobDifficulty[j - 1])
                    dp[i][k] = min(dp[i][k], dp[j - 1][k - 1] + max_diff)

        return dp[m][d]