class UnionFind(object):
    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.count = n

    def find(self, child):
        if self.father[child] == child:
            return child
        self.father[child] = self.find(self.father[child])
        return self.father[child]

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            self.count -= 1


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 判断图是否是树，首先课树有x个点，x-1条边，其次图内所有点都连通且无环
        if n - 1 != len(edges):
            return False
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)

        return uf.count == 1