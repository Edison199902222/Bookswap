class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0
        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    visited[i][j] = True
                    self.dfs(i, j, grid, grid[i][j], visited)
                    visited[i][j] = False
        return self.res

    def dfs(self, i, j, grid, sums, visited):
        self.res = max(self.res, sums)
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = i + x
            new_y = j + y
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (not visited[new_x][new_y]) and grid[new_x][
                new_y] != 0:
                visited[new_x][new_y] = True
                self.dfs(new_x, new_y, grid, sums + grid[new_x][new_y], visited)
                visited[new_x][new_y] = False


'''
套路题，每一次dfs 我们就更新result
用visited 去设置 表示当前的点我们已经走过了 不能再走了
遍历我们的grid 寻找不为0 的格子， 作为我们的起始点， 一个一个去尝试
记得每一次visited 需要还原
'''
