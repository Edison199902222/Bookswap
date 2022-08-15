class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m = len(S)
        n = len(T)
        # dp[i][j] 表示 s的前i个元素 跟 t的前 j 个 minimum window 是多少
        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]
        # 两个空串 啃噬0
        dp[0][0] = 0
        # t如果是空的话，也是0
        for i in range(m + 1):
            dp[i][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 相等的话，
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 说明S[j]没有帮助，还要依靠dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + 1

        min_length = float("inf")
        index = 0
        # 最后在所有dp[N][j]中找到第一个最小值k，那么 S.substr(j-k+1,k)就是答案
        # 因为第一个最小值k出现的最后一个index 肯定是t的结尾元素
        for i in range(1, m + 1):
            if dp[i][n] < min_length:
                min_length = dp[i][n]
                index = i

        if min_length == float("inf"):
            return ""
        return S[index - min_length: index]

