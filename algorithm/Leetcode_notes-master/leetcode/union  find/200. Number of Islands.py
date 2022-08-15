'''
可以用染色（dfs）或者union find去做
'''


class UnionFind(object):
    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.count = n

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            self.count -= 1

    def find(self, child):
        if self.father[child] == child:
            return child
        # 路径压缩，不用全部往上找
        self.father[child] = self.find(self.father[child])
        return self.father[child]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    # 不是岛的话， count 直接 - 1
                    uf.count -= 1
                    continue
                # 算出对应的岛屿number
                number_island = i * n + j
                if i < m - 1 and grid[i + 1][j] == "1":
                    uf.union(number_island, number_island + n)
                if j < n - 1 and grid[i][j + 1] == "1":
                    uf.union(number_island, number_island + 1)

        return uf.count
if __name__ == '__main__':
    solution = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(solution.numIslands(grid))