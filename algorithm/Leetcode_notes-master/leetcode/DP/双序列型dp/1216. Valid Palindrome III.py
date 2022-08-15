class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        '''
        此题和1312题很相似的想法。想要将一个字符串s变成一个回文串（无论是通过增加还是删除），
        一个技巧就是构造另一个字符串t是s的逆序。于是，如果要求增加字符，
        那么s和t的shorted common supersequence就是需要增加的最少字符；如果要求删除字符，那么s和t的longest   
        common subsequence就对应着需要删除的最少字符。
        本题求出s和t的LCS后，只需要判断s的长度减去LCS的长度（即对于s而言最少需要删除的字符）是否小于等于k即可。
        '''
        t = s[::-1]
        m = len(s)
        n = len(t)
        # dp[i][j] s的前i 个 跟t 的前j 个的 lcs 有多长
        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # 知道 s 跟t 的lcs 之后， 用s 的长度 减去 lcs 就是要减去几个字符了
        lcs_length = dp[m][n]
        if len(s) - lcs_length <= k:
            return True
        return False