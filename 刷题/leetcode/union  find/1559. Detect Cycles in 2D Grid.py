class Union_Find():
    def __init__(self, n):
        self.father = {i: i for i in range(n)}

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        father_a, father_b = self.find(a), self.find(b)
        if father_a == father_b:
            return True
        self.father[father_b] = father_a
        return False


# union find 可以检测无向图有没有环
class Solution(object):
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        uf = Union_Find(m * n)
        for i in range(m):
            for j in range(n):
                # 检查左边 跟上面，并且如果是一样的letter 的话，union 到一起
                # 如果左边 或者上面，父亲 node 是相同的话，说明形成了一个环！
                if i > 0 and grid[i][j] == grid[i - 1][j] and uf.union(i * n + j, (i - 1) * n + j):
                    print(i, j, 1)
                    return True
                if j > 0 and grid[i][j] == grid[i][j - 1] and uf.union(i * n + j, i * n + j - 1):
                    print(i, j, 2)
                    return True
        return False
