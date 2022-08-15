class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 第一步 对于每个group 找到对应的item， 并且没有goup的item 分配一个
        group_match = collections.defaultdict(set)
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group_match[group[i]].add(i)
        # 第二步， 通过beforeitems，对于在同一个group中的，找到对应关系，不在一个group中的 找到group之间的关系
        team_degree, team_graph = collections.defaultdict(int), collections.defaultdict(set)
        group_degree, group_graph = collections.defaultdict(int), collections.defaultdict(set)
        for i in range(n):
            # j 要出现在i前面！！！
            for j in beforeItems[i]:
                # 如果同在一个group
                if group[i] == group[j]:
                    team_graph[j].add(i)
                    team_degree[i] += 1
                # 不在一个group
                else:
                    # group 会有重复的边
                    # 意思是，一个group 有可能会反复添加degree， 所以先要判断这条边是不是已经在里面了
                    if group[i] in group_graph[group[j]]:
                        continue
                    group_graph[group[j]].add(group[i])
                    group_degree[group[i]] += 1
        print(group_degree, group_graph)
        # 第三步，先对group 进行topo sort， 找出group之间的关系
        group_order = self.topo_sort([i for i in group_match], group_degree, group_graph)
        # 第四步，对group 内部进行排序
        result = []
        for i in group_order:
            items = group_match[i]
            team_order = self.topo_sort(items, team_degree, team_graph)
            if len(items) != len(team_order):
                return []
            result += team_order
        return result if len(result) == n else []

    def topo_sort(self, points, degree, graph):
        order = []
        start_node = [p for p in points if degree[p] == 0]
        queue = collections.deque(start_node)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == len(points) else []
