class union_find:
    def __init__(self):
        self.father = {}
        self.count = 0
        self.rank = {}

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.rank[a] += self.rank[b]
        self.father[b] = a
        self.count -= 1

    def union_and_find(self, a, b):
        father_a, father_b = self.find(a), self.find(b)
        if father_a != father_b:
            self.union(father_a, father_b)
            return False
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = union_find()
        result = []
        for x, y in edges:
            if x not in uf.father:
                uf.father[x] = x
                uf.rank[x] = 1
                uf.count += 1
            if y not in uf.father:
                uf.father[y] = y
                uf.rank[y] = 1
                uf.count += 1
            if uf.union_and_find(x, y):
                return [x, y]
        return result

