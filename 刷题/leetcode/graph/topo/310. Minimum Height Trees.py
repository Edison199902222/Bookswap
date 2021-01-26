import collections

# time ：O(E + V)
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # building graph
        graph = {x: [] for x in range(n)}
        # 剥洋葱， 其实看的是degree 而不仅仅是in degree  或者 out degree
        in_degree = {x: 0 for x in range(n)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            in_degree[i] += 1
            in_degree[j] += 1
        start_node = [x for x in range(n) if in_degree[x] <= 1]
        # BFS
        queue = collections.deque(start_node)
        result = []
        while queue:
            current_result = []
            for i in range(len(queue)):
                node = queue.popleft()
                current_result.append(node)
                for neighbour in graph[node]:
                    in_degree[neighbour] -= 1
                    if in_degree[neighbour] == 1:
                        queue.append(neighbour)
            result = current_result
        return result
'''
无向图也可以使用拓扑排序
不一样的是， 对于有向图来说，我们排除入度为0的
但无向图是双向的， 我们得每次排除入读为1的
所以 我们每一次 排除 入度为1 的 并且我们必须保存每一层 入度相同的node
因为在最后一层， 我们输出的node 有可能不止一个， 有可能2 个都是入读为1 的node
'''
