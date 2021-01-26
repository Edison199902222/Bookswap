class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.memo = {}
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        return self.dfs(0, 0, n - 1, m, n, grid)

    def dfs(self, i, x, y, m, n, grid):
        if i == m:
            return 0
        if (i, x, y) in self.memo:
            return self.memo[i, x, y]
        res = 0
        if x == y:
            res += grid[i][x]
        else:
            res += grid[i][x] + grid[i][y]
        next = 0
        for new_x in range(-1, 2):
            for new_y in range(-1, 2):
                a = x + new_x
                b = y + new_y
                if 0 <= a <= b and b < n:
                    next = max(next, self.dfs(i + 1, a, b, m, n, grid))
        res += next
        self.memo[i, x, y] = res
        return res
