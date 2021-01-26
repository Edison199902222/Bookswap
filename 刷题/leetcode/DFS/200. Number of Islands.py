'''
被水包围的才算是一个land
染色来做
遍历网格 遇到水就跳过
然后遇到岛屿就dfs 把所有附近的岛屿跟自己 全部染成0 这样以防重复访问 然后count+1
最后返回count
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                self.dfs(i, j, grid)
                count += 1
        return count

    def dfs(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.dfs(i+1,j,grid)
        self.dfs(i-1,j,grid)
        self.dfs(i,j+1,grid)
        self.dfs(i,j-1,grid)
