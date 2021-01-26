class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # 两次bfs 找树的 最大直径 是指某两个点之间的距离，
        # 找到任意点 a， 找到a的最远距离node b， b肯定是 最远直径的两个点之一，然后再以b找到最远距离的node c，
        # b c 之间就是最大直径
        # 因为是一个树，任意点 有三种情况， 树的头， 中间，跟尾巴
        # 如果树的头是的话，那么最远的点是尾巴，尾巴跟头肯定是最大直径
        # 如果树的中间是任意点的话，最远的点是尾部或者头，那么也肯定是最大直径之一
        # 如果树的尾巴是任意点的话，最远的点是头，那么头肯定是最大直径的两个点之一
        start_node = [0]
        queue = collections.deque(start_node)
        prev = 0
        visited = set()
        visited.add(0)
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            prev = node
        start_node = [(prev, 0)]
        queue = collections.deque(start_node)
        visited = set()
        visited.add(prev)
        result = 0
        while queue:
            node, dia = queue.popleft()
            result = max(result, dia)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dia + 1))
        return result