class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # 题目要求 找到所有 out degree 为0的node
        # 逆向拓扑排序
        graph_dic = collections.defaultdict(list)
        out_degree = collections.defaultdict(int)
        # 第一步 建立图， 并且建立out degree
        for i in range(len(graph)):
            out_degree[i] += len(graph[i])
            # 第二步，因为是 out degree， 所以要反转
            for reverse in graph[i]:
                graph_dic[reverse].append(i)
        # 第三步 把所有out degree 为0的node  放进去
        start_node = [x for x in out_degree if out_degree[x] == 0]
        queue = collections.deque(start_node)

        result = []
        # 遍历
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph_dic[node]:
                out_degree[neighbor] -= 1
                if out_degree[neighbor] == 0:
                    queue.append(neighbor)
        return sorted(result)
