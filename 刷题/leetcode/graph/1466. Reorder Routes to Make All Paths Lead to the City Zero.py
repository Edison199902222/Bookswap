import collections


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(set)
        edges = collections.defaultdict(set)
        for start, to in connections:
            graph[start].add(to)
            edges[start].add(to)
            edges[to].add(start)
        queue = collections.deque([0])
        result = 0
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in edges[node]:
                if neighbor in visited:
                    continue
                if node not in graph[neighbor]:
                    result += 1
                visited.add(neighbor)
                queue.append(neighbor)
        return result