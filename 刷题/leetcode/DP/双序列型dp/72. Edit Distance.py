'''
状态：DP[i][j]
i：表示word1 的前i个字符
j：表示word2 的前j个字符
所以 总共表示 word1 的i字符 变成word2 的j字符 最少需要的次数
建立dp数组时， 需要多建立一个， 因为我们代表的是字符的第几个字符， 而不是index
我们 遍历两个字符
如果发现 i - 1 == j- 1 也就是当前字符相等，
dp【i][j]就会等于， 第一种情况 我们第一个字符前i - 1跟 第二个字符的j匹配的最少次数 再把最后一个字符i remove了 也就是 + 1
第二种情况 我们第一个字符的前i 个 跟第二个字符的j - 1 个字符匹配，然后把最后一个字符添加进来，也就是 + 1
第三种情况 我们把前i - 1 个字符 跟 j - 1 个字符匹配的最少次数 再加上因为 第i 个 == 第j 个
以上三种情况 的最少值就是dp i j
如果i - 1 ！= j - 1的话
也是三种情况
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for i in range(n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    # dp[i - 1][j] + 1 代表 i -1 跟 j 匹配后，把第i 个 remove
                    # dp[i][j - 1] + 1 代表 i 跟 j - 1 匹配后，增加一个字符
                    # dp[i - 1][j - 1] + 1 代表 i - 1 跟 j - 1 匹配后 replace
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance("horse","ros"))