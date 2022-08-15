'''
状态：DP[i][j]
i：表示word1 的前i个字符
j：表示word2 的前j个字符
所以 总共表示 word1 的i字符 变成word2 的j字符 最少需要的次数

'''


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1) ]
        for i in range(m+1): dp[i][0] = i
        for j in range(n+1): dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[m][n]

if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance("horse","ros"))