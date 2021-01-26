class Union_Find():
    def __init__(self):
        self.father = {}

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            self.count[father_a] += self.count[father_b]

def first_question(edges):
    uf = Union_Find()
    for start, end in edges:

