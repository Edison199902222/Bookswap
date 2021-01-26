class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # prim 是从 点到点，保持联通区域走下去
        n = len(points)
        graph = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((cost, j))
                graph[j].append((cost, i))
        visited = set()
        # 起点任意设置
        visited.add(0)
        heap = []
        for i in graph[0]:
            heapq.heappush(heap, i)
        result = 0
        while heap:
            # 拿出当前cost 最小 可以去的node
            cost, node = heapq.heappop(heap)
            # 如果没去过的话， 那么就去
            if node not in visited:
                visited.add(node)
                result += cost
                # 把新的node 的边也放进heap 中
                for new_node in graph[node]:
                    heapq.heappush(heap, new_node)
            if len(visited) >= n:
                break
        return result

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


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        # 建立 边的关系图
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph.append([i, j, cost])
        n = len(points)
        result = 0
        uf = union_find(n)
        # 排序边，然后遍历
        for edge in sorted(graph, key=lambda x: x[2]):
            # 用uf 来检查当前边链接的两个点是否联通
            if not uf.union_andfind(edge[0], edge[1]):
                # 不联通就加上cost
                result += edge[2]
        return result


