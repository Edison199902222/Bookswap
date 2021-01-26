class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = len(s)
        # dp[i][j] 意思是 s的第i 个元素 到第j个元素 的 Longest Palindromic Subsequence
        dp = [[0] * (m + 1) for i in range(m + 1)]
        # 枚举长度
        for length in range(1, m + 1):
            # 找起始位置, 起点最多能设置到哪
            for i in range(1, m - length + 2):
                # 找到终止位置 j
                j = i + length - 1
                # 如果长度为1，那么回文的长度肯定是1
                if length == 1:
                    dp[i][j] = 1
                # 如果最左边的跟最右边的相等，那么肯定取决于里面的是不是相等
                elif s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                # 如果不相等，那么取决于i 和 j肯定 至少有一个不是subsequecnce 中的一员
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[1][m]