class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        self.memo = {}
        return self.dfs(A, B, m - 1, n - 1)

    def dfs(self, A, B, i, j):
        if i < 0 or j < 0:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i == j and i == 0 and j == 0 and A[i] == B[j]:
            return 1
        elif i == j and i == 0 and j == 0 and A[i] != B[j]:
            return 0
        result = 0
        if A[i] == B[j]:
            result = max(result, self.dfs(A, B, i - 1, j - 1) + 1)
        result = max(result, self.dfs(A, B, i - 1, j - 1), self.dfs(A, B, i - 1, j), self.dfs(A, B, i, j - 1))
        self.memo[(i, j)] = result
        return result
'''
跟lcs的规律是一样的
dp[i][j]表示 A 的第i位 跟 B 的第j位 最大 uncrossed line的情况
我们考虑到，不能cross line的话， 对于A的第i 位来说，我们不能跟 B的 j + 1 位匹配， 因为这样匹配的话，有可能会出现cross line 的情况
所以 对于第i 位我们有三种选择， 一种是跟第j 位匹配，一种是跟第j - 1位匹配， 一种是 i - 1 跟 第j 位匹配
如果第i位跟 第j 位是相等的话
那么我们就i 跟j 匹配， dp[i][j] = dp[i-1][j-1] + 1

'''


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        # dp[i][j] 表示 A的前i个数字 跟B的前j个数字 最多有多少条线
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果可以连线，那么取决于i - 1 跟 j - 1 因为不能交叉
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 如果i j 不能相连，那么看 i - 1 跟 j 最多有几条线
                # i  跟 j - 1 最多有几条线
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]