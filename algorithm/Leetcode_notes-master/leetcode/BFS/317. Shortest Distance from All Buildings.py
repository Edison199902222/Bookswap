class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 一个matrix 记录land 到 building距离的情况
        # 一个matrix 记录下每个land 访问了几个building
        m = len(grid)
        n = len(grid[0])
        distance = [[float("inf")] * n for i in range(m)]
        build_number = [[0] * n for i in range(m)]
        building = 0
        # 从每一个building 出发 计算累加每个building 到每个点的距离
        # 并且更新 build matrix 记录有几个building 能到 当前点
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, distance, build_number, i, j)
                    building += 1
        result = float("inf")
        # 只有距离小于当前的最小距离 并且 当前点 可以被所有build 访问到 才可以更新result
        for i in range(m):
            for j in range(n):
                if distance[i][j] < result and build_number[i][j] == building:
                    result = distance[i][j]

        return result if result != float("inf") else - 1

    def bfs(self, grid, distance, build_number, i, j):
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for k in range(m)]
        visited[i][j] = True
        queue = collections.deque()
        queue.append((i, j, 0))
        while queue:
            x, y, cur_dis = queue.popleft()
            # 如果distance 等于float 说明 第一次访问这个点，变0
            if distance[x][y] == float("inf"):
                distance[x][y] = 0
            # 累加
            distance[x][y] += cur_dis
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                # 不能走回头路，并且只能走空地
                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] != True and grid[new_x][new_y] == 0:
                    queue.append((new_x, new_y, cur_dis + 1))
                    # 更新build，说明一个building 可以走到当前点
                    build_number[new_x][new_y] += 1
                    visited[new_x][new_y] = True
        return


'''
使用bfs
我们用distance 算出每一个 empty land 到 building 的距离
reach building  意思是 每个 empty land 可以reach 几个building
我们先遍历数组
如果遇到 building的话
我们就以building  为起点 进行bfs 把所有可以到的的空地 进行操作 并且building数量要加1 统计有几个building
并且操作之前 先建立visit 二维数组 来减枝 
然后把 当前的起点 放进queue中，每一个node 是由坐标 以及距离起点的距离组成的
每一次 pop 一个node 出来 先把当前node 的distance 进行累加 表示 这个点现在最少需要 i 个距离到各个点
然后以这个node进行上下左右搜索   如果合法的话 先把合法搜索出来的点 在visit 数组中设置为true
然后判断 是不是空地 
如果是空地的话 我们把它放进quenue 中 并且 node 中的距离 是要加1 的
然后搜索出来的node 在reach building 中 加1 表示 有一个building 可以到达这个空地

bfs结束后
我们遍历数组 判断 如果distance 是小于 我们的当前最小distance的话 并且 这个点可以到达我们所有的building的话
那么我们进行更新
'''