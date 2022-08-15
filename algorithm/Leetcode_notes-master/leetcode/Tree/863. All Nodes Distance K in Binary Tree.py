# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # 把本题看成graph， 先建立graph
        graph = collections.defaultdict(list)
        self.build_graph(graph, None, root)
        queue = collections.deque()
        queue.append([target, 0])
        visited = set()
        visited.add(target)
        result = []
        # 图建立完成后，利用bfs 去找距离为k的节点
        while queue:
            node, dis = queue.popleft()
            if dis == K:
                result.append(node.val)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append([neighbor, dis + 1])
        return result

    def build_graph(self, graph, parent, root):
        # 把当前root 跟 父亲节点链接
        if parent is not None:
            graph[root].append(parent)
        # 把root 跟 孩子节点链接
        if root.left:
            graph[root].append(root.left)
            self.build_graph(graph, root, root.left)
        if root.right:
            graph[root].append(root.right)
            self.build_graph(graph, root, root.right)
        return