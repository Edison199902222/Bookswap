class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        # 思路： 找到每个颜色边界，就可以知道这个颜色的矩阵大概是什么样子
        # 矩阵内每个格子 如果最后呈现的不是当前颜色，证明 当前颜色在之前一定出现过 只是后面被染色了
        # 这就有点像对应边关系了，比如一个格子 最后的颜色是4，但是它也被颜色1 的矩阵包括在内了
        # 所以，可以建立边 1 - > 4 ， 如果有一个格子 对应关系是 4 - > 1 这就说明我们无法找出这样一个order
        # 既 1 出现在4 之前，又4 出现1 之前 无法找到 所以return false
        # 如果可以找到一组order，使得整个矩阵合法， 那么return true，可以使用拓扑排序去寻找
        # 如果最后我们可以遍历所有的颜色， 那么说明可以达到预期的效果，如果有环，就不能
        graph = {i: [] for i in range(61)}
        in_degree = {i: 0 for i in range(61)}
        N = 61
        m = len(targetGrid)
        n = len(targetGrid[0])
        # 每个颜色 去看边界在哪，并且找出边界矩阵内 不一样的颜色，把他放进graph中
        for i in range(N):
            self.build_graph(i, graph, in_degree, targetGrid)
        start_node = [x for x in range(N) if in_degree[x] == 0]
        queue = collections.deque(start_node)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return count == N

    def build_graph(self, color, graph, in_degree, grid):
        m = len(grid)
        n = len(grid[0])
        x1, y1 = m, n
        x2, y2 = -1, -1
        # 寻找当前颜色 的matrix 边界
        for i in range(m):
            for j in range(n):
                if grid[i][j] == color:
                    x1, y1 = min(x1, i), min(y1, j)
                    x2, y2 = max(x2, i), max(y2, j)
        if x1 == m:
            return
            # 为了防止已经出现的颜色 不重复添加
        visited = set()
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                cur_c = grid[i][j]
                if cur_c != color and color not in visited:
                    graph[color].append(cur_c)
                    in_degree[cur_c] += 1
                    visited.add(cur_c)
        return



