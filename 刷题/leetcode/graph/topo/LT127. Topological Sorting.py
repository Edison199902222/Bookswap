"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
import collections
'''
拓扑排序的基础题
是一个bfs 加 topo的模版
先用字典建立 degree的图 
然后找到start node， 用queue 去把 入度为0 的pop 出来加入result后，再去掉 它邻居node 的入度
'''

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        degree_graph = self.graph_indegree(graph)
        start_node = [x for x in graph if degree_graph[x] == 0]
        queue = collections.deque(start_node)
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                degree_graph[neighbor] -= 1
                if degree_graph[neighbor] == 0:  # 如果去除当前node的入度以后， neighbor的入度也变成0的话 那么加入queue中
                    queue.append(neighbor)
        return result

    def graph_indegree(self, graph):
        dic = {x: 0 for x in graph}  # 创建degree 的图
        for node in graph:
            for neighbor in node.neighbors:
                dic[neighbor] += 1  # 没有邻居连到当前node的话，node的入度就是0
        return dic


"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

'''
dfs + topo
'''
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        degree_graph = {x: 0 for x in graph}
        for node in graph:
            for neighbors in node.neighbors:
                degree_graph[neighbors] += 1
        self.result = []
        for node in graph:
            if degree_graph[node] == 0:
                self.dfs(node, degree_graph)
        return self.result

    def dfs(self, node, degree_graph):
        self.result.append(node)
        degree_graph[node] -= 1  # 防止入度为0 的node 再次被访问
        for neighbors in node.neighbors:
            degree_graph[neighbors] -= 1
            if degree_graph[neighbors] == 0:
                self.dfs(neighbors, degree_graph)