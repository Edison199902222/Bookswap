class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 四维dp迷宫
        self.memo = {}
        # return 的是 当两个人同时走到终点的时候的最大收益
        return max(0, self.dfs(0, 0, 0, 0, grid, len(grid), len(grid[0])))

    def dfs(self, x1, y1, x2, y2, grid, m, n):
        # 想象两个人同时从 0，0 走到右下
        # 因为只能往下走或者往右走， 并且每次只能走一步 所以 x1 + y1 = x2 + y2
        # 用x1, y1, x2 就能够表示x1, y1, x2, y2 因为y2 = x1 + y2 - x2
        if x1 == m - 1 and y1 == n - 1:  # 当有一个人走到终点时，直接return
            return grid[x1][y1]
        if (x2 == m - 1 and y2 == n - 1):
            return grid[x2][y2]
        if x1 >= m or y1 >= n or x2 >= m or y2 >= n:
            return float("-inf")
        if grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return float("-inf")
        if (x1, y1, x2) in self.memo:
            return self.memo[(x1, y1, x2)]

        result = 0

        result = max(self.dfs(x1 + 1, y1, x2 + 1, y2, grid, m, n), self.dfs(x1 + 1, y1, x2, y2 + 1, grid, m, n),
                     self.dfs(x1, y1 + 1, x2 + 1, y2, grid, m, n), self.dfs(x1, y1 + 1, x2, y2 + 1, grid, m, n))

        if grid[x1][y1] == 1:
            result += 1
        if grid[x2][y2] == 1 and x1 != x2:
            result += 1
        self.memo[(x1, y1, x2)] = result

        return result
