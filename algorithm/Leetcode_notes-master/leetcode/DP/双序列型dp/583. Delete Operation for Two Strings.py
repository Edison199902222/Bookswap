class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j]表示 word1 前i个元素 很 word2 的前j个元素 minimum number of steps
        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]
        # 初始化，需要i次操作，因为word2 是0
        for i in range(m + 1):
            dp[i][0] = i
        # 同上
        for i in range(n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 相等的话，取决于前面
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 不等，取决于 是否要删除i，跟是否删除j 的最小值
                # 前者意思是，i - 1 跟j 匹配好，删除i
                # 后者意思是 i 跟 j - 1匹配相等， 删除j
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        return dp[m][n]
