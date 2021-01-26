class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]
'''
dp[i][j]表示 当前走到第i j 个格子 我们所需要多少种走法
那么 我们转化方程可以表示为
如果 当前格子不为 0的话
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
我们可以把它拆开来加 
如果 当前格子不是第一行 或者不是第一列的话， 那么 我们可以拆开成
dp[i][j] += dp[i - 1][j]
dp[i][j] += dp[i][j - 1]
如果 是 第一行 或者 第一列的话， 那么 我们这两个方程就只能满足一个。因为第一行的话，每个格子只能由最左边得到
我们初始化 左上角肯定是1 因为如果是0 的话 没有办法走到左上 这题没有办法解了
然后遍历array 遇到1的时候，我们就把dp[i][j]设置为0
然后 分成两种情况 i 》0 跟 j 》0
'''

'''
然后我们发现 我们可以使用滚动数组优化到 空间 On
其实每一行的值 只跟上一行有关系
dp[j]表示 能去 当前这一行第j 列 格子的方法有多少种
我们发现 如果 当前格子满足 i 大于0 j 也大于0 那么 去当前格子的方法其实是由左边 跟上面决定的了  
dp[j] += dp[j - 1] 因为我们是一维数组，我们使用累加的话 其实已经把上面格子的方法累加起来了，所以只需要加左边的
如果 j 》 0 的话，那么我们去当前格子方法数量 只是由左边决定
如果 i 》0的话 我们当前格子是由上面决定， 我们使用dp 一维数组已经代表了上面那一行，所以如果仅仅 i>0我们并不需要干任何事情
比如dp = [1,2,3] 当我们去 下一行时， i = 1，j = 0 我们其实i j 这个格子 的数量就是等于1，也就是等于dp[j]， 不需要加任何东西
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or len(obstacleGrid) == 0 or not obstacleGrid[0] or len(obstacleGrid[0]) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for j in range(n)]
        dp[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue

                if i > 0 and j > 0:
                    dp[j] += dp[j - 1]
                    continue

                if j > 0:
                    dp[j] = dp[j - 1]

        return dp[n - 1]

'''
dfs + memo
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        self.memo = {}
        return self.dp(0, 0, obstacleGrid)

    def dp(self, i, j, grid):
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1

        result = 0
        for x, y in [(i + 1, j), (i, j + 1)]:
            if len(grid) > x >= 0 and len(grid[0]) > y >= 0 and not grid[x][y]:
                result += self.dp(x, y, grid)
        self.memo[(i, j)] = result
        return result