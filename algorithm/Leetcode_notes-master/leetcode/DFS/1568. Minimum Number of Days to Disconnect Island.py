class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 一共就三种情况
        # 如果里面 不是只有一个岛屿的话，直接return 0
        # grid 只有一个岛屿，尝试去除去一个岛屿，再统计岛屿数量，如果不为1 return1
        # 如果去除一个岛屿没办法使得岛屿完成要求的话，return 2， 因为对任何一个的岛屿， 拆掉对角线，肯定可以拆开
        if self.count(grid) != 1:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    grid[i][j] = 0
                    if self.count(grid) != 1:
                        return 1
                    grid[i][j] = 1
        return 2

    def count(self, grid):
        island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                if grid[i][j] == 1:
                    island += 1
                    self.dfs(i, j, grid, visited)
        return island

    def dfs(self, i, j, grid, visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited or grid[i][j] != 1:
            return
        visited.add((i, j))
        self.dfs(i + 1, j, grid, visited)
        self.dfs(i - 1, j, grid, visited)
        self.dfs(i, j + 1, grid, visited)
        self.dfs(i, j - 1, grid, visited)
        return