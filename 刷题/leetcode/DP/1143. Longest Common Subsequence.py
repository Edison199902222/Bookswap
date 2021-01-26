class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]

'''
dp[i][j意思是 text1的 从 0 到 i 跟 text2 的从 0 到j 的最大相同的substring 是多少
为什么 我们的dp数组 会在最后 多几个0呢 是因为 当遍历到index = 0 的时候， 我们dp 是依据前面的状态来进行的， 0 - 1 会等于 -1 而dp【-1】
那么 遍历text1 跟 text2 如果发现当前text 的i 跟text2 的j 字符 是相等的， 那么我们可以推论 text1 从0 到j 的字符 跟text2 从0 到j 的字符的最大相同subsequence 
是由text1 从0 到 i- 1 跟 text2 从0 到j - 1 的最大相同subsequence + 1 因为 i 跟 j的字符是相等的 所以 i j 去掉 我们需要看 i -1 跟 j -1 的lcs
如果不相等的话 那么 我们就要考虑 i - 1 跟 j 的lcs 还有 i 跟 j - 1 的lcs
为什么呢 
比如 acef abc 当 i = 2 j = 2的时候 e跟c 不相等， 所以我们要考虑 ace 跟 ab的lcs 还有 ac 跟 abc的lcs
'''