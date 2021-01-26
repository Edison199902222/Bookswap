


"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
'''
做两件事情 
先看 node 在不在新的图之中
不在的话 node 加入到新的图之中
然后同时 把这个node加入之前node的邻居之中 

'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        new_graoh = {}
        stack = [node]
        visited = set()
        while stack:
            cur_node = stack.pop()
            if cur_node not in new_graoh:
                new_graoh[cur_node] = Node(node.val,[])
            if cur_node in visited:
                continue
            visited.add(cur_node)
            for neighbour in cur_node.neighbors:
                if neighbour not in new_graoh:
                    new_graoh[neighbour] = Node(neighbour.val,[])
                new_graoh[cur_node].neighbors.append(new_graoh[neighbour])
                stack.append(neighbour)
        return new_graoh[node]


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return node
        root = node
        nodes = self.get_node(node)  # 得到所有的node
        graph = {}
        for node in nodes:  # 复制新的node
            graph[node] = Node(node.val, [])
        # 把对应的neighbour 全部 复制上去
        for node in nodes:
            new_node = graph[node]
            for neighbour in node.neighbors:
                neighbour_new = graph[neighbour]
                new_node.neighbors.append(neighbour_new)
        return graph[root]

    def get_node(self, node):
        result = set([node])
        queue = collections.deque([node])
        while queue:
            head = queue.popleft()
            for neighbour in head.neighbors:
                if neighbour not in result:
                    result.add(neighbour)
                    queue.append(neighbour)
        return result
