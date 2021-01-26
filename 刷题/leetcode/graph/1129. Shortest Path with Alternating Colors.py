class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # 二分图
        # 建立两个图
        graph_red = collections.defaultdict(list)
        graph_blue = collections.defaultdict(list)
        for x, y in red_edges:
            graph_red[x].append(y)
        for x, y in blue_edges:
            graph_blue[x].append(y)
        # 初始化
        result = [float("inf") for i in range(n)]
        queue = collections.deque()
        # 起点的话，红蓝两条路都可以走
        queue.append((0, 0))
        queue.append((0, 1))
        # 记录path 的长度
        step = -1
        visited = set()
        visited.add((0, 0))
        visited.add((0, 1))
        while queue:
            step += 1
            for i in range(len(queue)):
                node, color = queue.popleft()
                # 找到下一条路线的颜色
                if color == 0:
                    next_color = 1
                else:
                    next_color = 0
                result[node] = min(result[node], step)
                # 走下一条颜色
                if next_color == 1:
                    for neighbor in graph_blue[node]:
                        if (neighbor, next_color) not in visited:
                            queue.append((neighbor, next_color))
                            visited.add((neighbor, next_color))
                else:
                    for neighbor in graph_red[node]:
                        if (neighbor, next_color) not in visited:
                            queue.append((neighbor, next_color))
                            visited.add((neighbor, next_color))
        return [r if r != float("inf") else - 1 for r in result]

