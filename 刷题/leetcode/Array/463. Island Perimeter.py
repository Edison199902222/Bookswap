class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row_max = len(grid)
        col_max = len(grid[0])
        area = 0
        comm = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area += 1
                    if row > 0 and grid[row - 1][col] == 1:
                        comm += 1
                    if row < row_max - 1 and grid[row + 1][col] == 1:
                        comm += 1
                    if col >  0 and  grid[row][col - 1] == 1:
                        comm += 1
                    if col < col_max - 1 and grid[row][col + 1] == 1:
                        comm += 1
        return area * 4 - comm
'''
我们只需要找 每一个陆地的格子 能贡献多少个周长 然后把所有格子可以贡献的周长加一起
规律就是 对于一个格子 最大可以贡献4 的周长 但是 如果有一个邻居 就会变成3 以此类推
我们只需要找到每个格子 有多少个邻居 就可以知道 贡献多少个周长了
'''