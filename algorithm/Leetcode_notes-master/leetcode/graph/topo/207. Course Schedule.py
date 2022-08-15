
'''
dfs + topo
建立edge 跟degree
然后遍历
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge = {x: [] for x in range(numCourses)}  # 储存的是 x 可以去那些点
        degree = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edge[j].append(i)  # 因为j 可以去i 所以把i 放进j的list 中
            degree[i] += 1  # 因为是j 去 i， i的入度+ 1
        self.result = 0
        for i in range(numCourses):
            if degree[i] == 0:
                self.dfs(edge, degree, i)
        return self.result == numCourses

    def dfs(self, edge, degree, node):
        self.result += 1
        degree[node] -= 1 # 防止degree 为0 的节点反复被添加
        for neighbor in edge[node]:
            degree[neighbor] -= 1
            if degree[neighbor] == 0:
                self.dfs(edge, degree, neighbor)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[]for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[y].append(x)
        for i in range(numCourses):
            if not self.dfs(graph, visit, i):
                return False
        return True

    def dfs(self, graph, visited, i):
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
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True




'''
bfs 标准写法
'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edge = {x: [] for x in range(numCourses)} # 储存的是 x 可以去那些点
        degree = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            edge[j].append(i) # 因为j 可以去i 所以把i 放进j的list 中
            degree[i] += 1   # 因为是j 去 i， i的入度+ 1
        start_node = [x for x in range(len(degree)) if degree[x] == 0]
        queue = collections.deque(start_node)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in edge[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses
