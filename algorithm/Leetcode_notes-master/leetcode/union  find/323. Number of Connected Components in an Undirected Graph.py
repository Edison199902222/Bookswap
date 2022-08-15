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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for start, end in edges:
            uf.union(start, end)

        return uf.count