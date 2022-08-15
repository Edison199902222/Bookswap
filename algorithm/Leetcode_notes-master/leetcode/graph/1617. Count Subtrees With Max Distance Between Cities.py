class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        result = [0 for i in range(n - 1)]
        # bitmask， 0代表不选，1代表选
        for state in range(1, 1 << n):
            distance = self.get_distance(state, graph, n)
            if distance > 0:
                result[distance - 1] += 1
        return result

    # 得到所有选中的city
    def get_distance(self, state, graph, n):
        city = set()
        for i in range(n):
            if (state >> i) & 1 == 1:
                city.add(i)

        return self.get_dia(graph, city)

    # 两次bfs 找 树中最远直径
    # 第一次从任何a，找到最远距离的b
    # 然后从最远距离的node b 找到 b 的最远node c， b 到 c之间就是整个树的直径了
    def get_dia(self, graph, city):
        start_node = city.pop()
        city.add(start_node)
        farest_node, _, visited = self.bfs(graph, city, start_node)
        # 如果visited 不等于 city 的总数量，代表这个set 不是一个tree 不联通
        if len(visited) != len(city):
            return 0
        _, d, _ = self.bfs(graph, city, farest_node)
        return d

    # 两次bfs 找距离
    def bfs(self, graph, city, node):
        queue = collections.deque()
        farest_node = node
        queue.append((node, 0))
        d = 0
        visited = set()
        visited.add(node)
        while queue:
            node, distance = queue.popleft()
            d = max(d, distance)
            farest_node = node
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor in city:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return farest_node, d, visited