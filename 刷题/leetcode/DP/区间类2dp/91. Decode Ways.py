class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i][j] 长度为i 的string 有几种decode 的方法
        dp = [0 for i in range(n + 1)]
        # 长度为0的话，有1 种，就是空
        dp[0] = 1
        # 第一个字母如果是0，那就没办法decode
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, n + 1):
            # 如果当前字母是有效的话，那么现在的decode 的方法 就等于 前面的decode 的方法
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            sub_digit = int(s[i - 2:i])
            # 如果两个字母可以组成有效的话，那么加上前i - 2 长度的decode 方法
            if 26 >= sub_digit >= 10:
                dp[i] += dp[i - 2]
        return dp[n]