class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        # dp[i][j] s1的 前i 个 跟 s2 的前j 跟 能否交错形成s3 的前 i + j 个
        dp = [[False] * (n + 1) for i in range(m + 1)]

        dp[0][0] = True
        # 初始化
        # dp[i][0]表示从s1里取前i个，是否能与s3的前i个组成交叉子串。显然就是判断s1和s3是否逐位相等
        for i in range(1, m + 1):
            # 当前位s1 跟 s3 相等，如果s1 - 1 也能形成 s3 - 1， 那么就是对的
            if dp[i - 1][0] == True and s1[i - 1] == s3[i - 1]:
                dp[i][0] = True

        for i in range(1, n + 1):
            if dp[0][i - 1] == True and s2[i - 1] == s3[i - 1]:
                dp[0][i] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                elif s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                    dp[i][j] = True

        return dp[m][n]
