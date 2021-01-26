class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        visited = set()
        visited.add(0)
        end = len(graph) - 1
        self.dfs(visited, 0, [0], end, graph)
        return self.result

    def dfs(self, visited, cur, path, end, graph):
        if cur == end:
            self.result.append(path[:])
            return
        for neighbor in graph[cur]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                self.dfs(visited, neighbor, path, end, graph)
                visited.remove(neighbor)
                path.pop()
        return
