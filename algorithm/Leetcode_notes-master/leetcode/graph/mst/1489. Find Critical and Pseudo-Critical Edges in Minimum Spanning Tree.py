class union_find:
    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.count = n
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.rank[x] += self.rank[y]
        self.count -= 1
        self.father[y] = x

    def find_and_union(self, x, y):
        father_x, father_y = self.find(x), self.find(y)
        if father_x != father_y:
            self.union(father_x, father_y)
            return False
        return True


class Solution:
    def krukal(self, n, edges, skip_edge=None):
        uf = union_find(n)
        cost = 0
        if skip_edge != None:
            u, v, w = skip_edge
            cost += w
            uf.find_and_union(u, v)
        for u, v, w in edges:
            if not uf.find_and_union(u, v):
                cost += w
            if uf.count == 1:
                break
        return cost if uf.count == 1 else float("inf")

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 关键边是 不选这条边的话，mst 生成的 weight 会上升
        # 非关键边是，必须选这条边的情况下， 生成的mst 和最小mst weight 一样
        # 排序edge号
        order = sorted(range(len(edges)), key=lambda x: edges[x][2])
        edges = [edges[x] for x in order]
        min_cost = self.krukal(n, edges)
        critical = []
        pseudo = []
        # 暴力尝试，不选这条边，跟 一定选这条边 对cost 的影响
        for i in range(len(edges)):
            skip = edges[i]
            new_edge = edges[:i] + edges[i + 1:]
            # 去掉这条边 导致不联通 也会是关键边
            if self.krukal(n, new_edge) > min_cost:
                critical.append(order[i])
            elif self.krukal(n, new_edge, skip) == min_cost:
                pseudo.append(order[i])
        return [critical, pseudo]


