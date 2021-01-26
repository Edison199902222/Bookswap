import collections


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        node = set(x for seq in seqs for x in seq)
        graph = {x: [] for x in node}
        in_degree = {x: 0 for x in node}
        for relation in seqs:
            for i in range(len(relation) - 1):
                start = relation[i]
                end = relation[i + 1]
                graph[start].append(end)
                in_degree[end] += 1
        start_node = [x for x in node if in_degree[x] == 0]
        queue = collections.deque(start_node)
        result = []
        while queue:
            if len(queue) != 1:
                return False
            current = queue.popleft()
            result.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return len(result) == len(node) and result == org
