class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = s[::-1]
        m = len(s)
        n = len(t)
        # dp[i][j] s 的前 i个 跟 t的前j 个 shorted common supersequence 多长
        # shorted common supersequence 意思是， 创建一个 string 让s 跟 t 同时是subsequence
        #  scs 转化成了 s 跟t 加多少字符使他们相等， 因为 s 跟t 是逆序，并且加了一些字符 使他们都变成scs了
        # 那么他们一定是回文了
        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 因为相等，取一个作为scs就行
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # dp[i - 1][j] + 1 意思是 看 i - 1 跟 j 的scs， 然后加上一个i就是i j 的scs
                    # dp[i][j - 1] + 1 意思是 看i 跟j - 1 的scs， 加上一个j 就是i 跟j 的scs
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        scs_length = dp[m][n]
        return scs_length - m


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # 区间dp，定义dp[i][j]表示区间s[i:j]变成回文串最少需要多少添加多少字符
        dp = [[float("inf")] * (n + 1) for i in range(n + 1)]
        dp[0][0] = 0
        # 长度为1的时候
        for i in range(1, n + 1):
            dp[i][i] = 0
        # 初始化，枚举长度，
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                # 如果length 等于2, 两个字母又相等，自然等于0
                if length == 2 and s[i - 1] == s[j - 1]:
                    dp[i][j] = 0
                # 其他情况，i == j，取决于中间
                elif s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1]
                # 不相等的话，肯定要插入 i 或者j 让i 到 j 变成回文
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[1][n]


