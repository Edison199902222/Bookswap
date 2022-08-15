class Solution(object):
    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        # 先建立图， 通过dfs 来计算概率
        # 如果当前node 是叶子节点，并且是target 的话，t 有没有消耗完都没关系
        # 如果当前t 等于 0 并且cur node 是target 话 也可以更新结果
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        self.result = 0
        self.dfs(target, t, graph, 1, 1, visited)
        return self.result

    def dfs(self, target, time, graph, cur, pro, visited):
        if time <= 0:
            if cur == target:
                self.result = pro
            return
        # 当前 下一层的node 有几个
        k = len(graph[cur])
        # 建立图的时候把父节点也放进去了， 所以除了root以外，其他的要减去父节点
        if cur != 1:
            k -= 1
        if k == 0:
            if cur == target:
                self.result = pro
                return
        visited.add(cur)
        for neighbor in graph[cur]:
            if neighbor in visited:
                continue
            self.dfs(target, time - 1, graph, neighbor, pro * (1.0 / max(k, 1)), visited)
        visited.remove(cur)
        return


