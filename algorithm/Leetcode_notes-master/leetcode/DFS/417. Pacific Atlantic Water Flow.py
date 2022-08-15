
'''
先创建两个listlist
一个是大西洋 一个是太平洋初始化都是false
然后 一个 一个 去dfs
从边界的部分开始
然后 遍历整个网格 如果大西洋跟太平洋的listlist 都是true的话 才说明这个格子是true
'''


class Solution:
    def pacificAtlantic(self, matrix):
        # 题目要求的是，有多少河流是可以同时到达大西洋和太平洋？
        # 思路是逆流，从太平洋和大西洋同时逆流找路
        # 所以 正向的话，是只能从高到低
        # 反向的话，就是从低到高
        # 时间复杂度是mn，因为每个格子只会访问一次
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        pacific = [[False for i in range(n)] for i in range(m)]
        atlantic = [[False for i in range(n)] for i in range(m)]
        for i in range(m):
            self.dfs(i, 0, matrix, pacific)
            self.dfs(i, n - 1, matrix, atlantic)

        for i in range(n):
            self.dfs(0, i, matrix, pacific)
            self.dfs(m - 1, i, matrix, atlantic)
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, i, j, matrix, grid):
        grid[i][j] = True
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            # 规定从低到高流， 用grid 代替visited
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[i][j] > matrix[x][y] or grid[x][y]:
                continue
            self.dfs(x, y, matrix, grid)


if __name__ == "__main__":
    list1 = [[1,1],[1,1],[1,1]]
    solution = Solution()
    print(solution.pacificAtlantic(list1))