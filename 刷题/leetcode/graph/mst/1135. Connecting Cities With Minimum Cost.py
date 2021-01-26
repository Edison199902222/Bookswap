class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, c in connections:
            graph[u].append((c, v))
            graph[v].append((c, u))

        heap = []
        visited = set()
        result = 0
        for i in graph[1]:
            heapq.heappush(heap, i)
        visited.add(1)
        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            result += cost
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    heapq.heappush(heap, next_node)
            if len(visited) >= N:
                break
        return result if len(visited) == N else -1

'''
kruskal
'''


class union_find:
    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.rank = [1 for i in range(n)]
        self.count = n

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.rank[x] += self.rank[y]
        self.father[y] = x
        self.count -= 1

    def union_andfind(self, x, y):
        father_x, father_y = self.find(x), self.find(y)
        if father_x != father_y:
            self.union(father_x, father_y)
            return False
        return True


class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        uf = union_find(N)
        result = 0
        for edge in sorted(connections, key=lambda x: x[2]):
            if not uf.union_andfind(edge[0] - 1, edge[1] - 1):
                result += edge[2]
        return result if uf.count == 1 else -1
