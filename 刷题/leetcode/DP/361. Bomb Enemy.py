class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        up = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]
        left = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]
        # 统计左边炸死的人数
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "W":
                    if grid[i][j] == "E":
                        left[i][j] = 1
                    if j > 0:
                        left[i][j] += left[i][j - 1]
        # 统计右边炸死的人数
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if grid[i][j] != "W":
                    if grid[i][j] == "E":
                        right[i][j] = 1
                    if j < n - 1:
                        right[i][j] += right[i][j + 1]
        # 统计上面炸死的人数
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "W":
                    if grid[i][j] == "E":
                        up[i][j] = 1
                    if i > 0:
                        up[i][j] += up[i - 1][j]
        # 统计下面炸死的人数
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if grid[i][j] != "W":
                    if grid[i][j] == "E":
                        down[i][j] = 1
                    if i < m - 1:
                        down[i][j] += down[i + 1][j]
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    result = max(result, left[i][j] + right[i][j] + up[i][j] + down[i][j])
        return result
