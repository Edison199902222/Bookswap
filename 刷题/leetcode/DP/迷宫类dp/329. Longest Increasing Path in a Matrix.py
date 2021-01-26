class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # 因为不是从起点出发，不能使用单纯的dp, 用dfs + memo， dp代替了之前的字典
        if not matrix or not matrix[0]:
            return 0
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        # 当前格子最长的上升path 是多少
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                result = max(result, self.dfs(i, j, matrix, dp, m, n))
        return result

    def dfs(self, i, j, matrix, dp, m, n):
        # base case 如果当前dp[i][j]已经有结果了， 直接return， 避免重复搜索
        if dp[i][j]:
            return dp[i][j]
        # 先把自己设置成1， 因为自身就是1个， 所以至少有1 个
        dp[i][j] = 1
        if i - 1 >= 0 and matrix[i][j] > matrix[i - 1][j]:
            dp[i][j] = max(dp[i][j], self.dfs(i - 1, j, matrix, dp, m, n) + 1)
        if j - 1 >= 0 and matrix[i][j] > matrix[i][j - 1]:
            dp[i][j] = max(dp[i][j], self.dfs(i, j - 1, matrix, dp, m, n) + 1)
        if i + 1 < m and matrix[i][j] > matrix[i + 1][j]:
            dp[i][j] = max(dp[i][j], self.dfs(i + 1, j, matrix, dp, m, n) + 1)
        if j + 1 < n and matrix[i][j] > matrix[i][j + 1]:
            dp[i][j] = max(dp[i][j], self.dfs(i, j + 1, matrix, dp, m, n) + 1)
        return dp[i][j]

