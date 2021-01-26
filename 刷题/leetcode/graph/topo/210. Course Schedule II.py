'''
dfs 每次从一个node 出发， 找环
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        graph = {x: [] for x in range(numCourses)}
        for p in prerequisites:
            graph[p[1]].append(p[0])

        # collecting topological order
        ret = []
        for i in range(numCourses):
            if not self.dfs(graph,visited,i,ret):
                return []

        return ret[::-1]
    def dfs(self, graph, visited, i,ret):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph,visited,j,ret):
                return False
        # after visit all the neighbours, mark it as done visited
        ret.append(i)
        visited[i] = 1
        return True

'''
bfs标准
'''
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edge = {x: [] for x in range(numCourses)}  # 储存的是 x 可以去那些点
        degree = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edge[j].append(i)  # 因为j 可以去i 所以把i 放进j的list 中
            degree[i] += 1  # 因为是j 去 i， i的入度+ 1
        start_node = [x for x in range(len(degree)) if degree[x] == 0]
        queue = collections.deque(start_node)
        count = 0
        result = []
        while queue:
            node = queue.popleft()
            count += 1
            result.append(node)
            for neighbor in edge[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return result if count == numCourses else []

