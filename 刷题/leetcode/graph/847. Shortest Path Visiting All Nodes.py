class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        #技巧1： 使用 1<<i 指示路径中仅有节点i
        #技巧2： 想在旧的路径中增加新的节点，只需要 old_state | 1<<i 就把i位置变1了
        #技巧3： 宽度优先搜索的终止条件，全1的二进制数：1<<len(graph) - 1 就是了

        if not graph:
            return 0
        # 用当前点 和 到当前点为止走过的所有点作为状态 进行bfs
        start_node = [(i, 1 << i) for i in range(len(graph))]
        visited = collections.defaultdict(set)
        # 用bitmask，1代表当前点走过
        for i in range(len(graph)):
            visited[i].add(1 << i)
        queue = collections.deque(start_node)
        path = 0
        n = len(graph)
        # bfs 寻找最短路线
        while queue:
            for i in range(len(queue)):
                cur, state = queue.popleft()
                # 如果当前状态是走过所有点了，那么return
                if state == (1 << n) - 1:
                    return path
                # 如果不是走过所有点，那么遍历当前所有邻居，如果走去邻居的点的状态不一样，尝试走到邻居
                for neighbor in graph[cur]:
                    if (state | 1 << neighbor) not in visited[neighbor]:
                        visited[neighbor].add(state | 1 << neighbor)
                        queue.append((neighbor, state | 1 << neighbor))
            path += 1
        return 