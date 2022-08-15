'''
先初始化  第一列的值 等于上一个的值加上现在的值
第一行也等于 左边的值加上自己的值
每次更新dp min（up，left）+现在的值
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)]for i in range(m)]
        dp[o][o] = grid[0][0]
        for i in range(1,n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]