class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if p[i - 1] == "*" and dp[0][i - 1]:
                dp[0][i] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == "*":
                    # 表示空的时候
                    # s的前i个字符和p的前j - 1个字符匹配成功将 * 号替换成空串
                    flag1 = dp[i][j - 1]
                    # s的前i - 1 个字符和p的前j个字符匹配成功，*号替换的长度不限制
                    # 因为 * 可以替换无限的长度，所以 * 可以让 i 一直 -1，因为只要前面是匹配的，现在也肯定是匹配的
                    flag2 = dp[i - 1][j]
                    dp[i][j] = flag1 or flag2

        return dp[m][n]
