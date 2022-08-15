class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)
        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]
        dp[0][0] = 0
        sums = 0
        for i in range(1, m + 1):
            sums += ord(s1[i - 1])
            dp[i][0] = sums
        sums = 0
        for i in range(1, n + 1):
            sums += ord(s2[i - 1])
            dp[0][i] = sums

        sums = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        return dp[m][n]
