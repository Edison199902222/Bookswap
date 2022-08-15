class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        m = len(grid)
        n = len(grid[0])
        pos = [[1] * (n) for i in range(m)]
        neg = [[1] * (n) for i in range(m)]
        pos[0][0] = grid[0][0]
        neg[0][0] = grid[0][0]
        for i in range(1, m):
            if grid[i][0] > 0:
                pos[i][0] = pos[i - 1][0] * grid[i][0]
                neg[i][0] = neg[i - 1][0] * grid[i][0]
            elif grid[i][0] < 0:
                pos[i][0] = neg[i - 1][0] * grid[i][0]
                neg[i][0] = pos[i - 1][0] * grid[i][0]
            else:
                pos[i][0] = 0
                neg[i][0] = 0

        for i in range(1, n):
            if grid[0][i] > 0:
                pos[0][i] = pos[0][i - 1] * grid[0][i]
                neg[0][i] = neg[0][i - 1] * grid[0][i]
            elif grid[0][i] < 0:
                pos[0][i] = neg[0][i - 1] * grid[0][i]
                neg[0][i] = pos[0][i - 1] * grid[0][i]
            else:
                pos[0][i] = 0
                neg[0][i] = 0
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    pos[i][j] = max(pos[i - 1][j] * grid[i][j], pos[i][j - 1] * grid[i][j])
                    neg[i][j] = min(neg[i - 1][j] * grid[i][j], neg[i][j - 1] * grid[i][j])
                elif grid[i][j] < 0:
                    pos[i][j] = max(neg[i - 1][j] * grid[i][j], neg[i][j - 1] * grid[i][j])
                    neg[i][j] = min(pos[i - 1][j] * grid[i][j], pos[i][j - 1] * grid[i][j])
                else:
                    pos[i][j] = 0
                    neg[i][j] = 0
        return max(pos[m - 1][n - 1], neg[m - 1][n - 1]) % (mod) if max(pos[m - 1][n - 1],
                                                                        neg[m - 1][n - 1]) >= 0 else - 1
