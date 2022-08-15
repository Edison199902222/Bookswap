class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        new_queue = []
        visited = set()
        time = 0
        direction = [(-1,0), (1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
        while queue:
            node = queue.pop(0)
            visited.add(node)
            for dir in direction:
                new_row = node[0] + dir[0]
                new_col = node[1] + dir[1]
                if 0 <= new_row < row  and 0 <= new_col < col and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    grid[new_row][new_col] = 2
                    new_queue.append((new_row, new_col))
            if len(queue) == 0 and new_queue:
                    time += 1
                    queue = new_queue
                    new_queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return time
'''
用bfs
先把所有坏掉的橘子加入进队列中
建立一个set 表示所有访问过的节点
然后开始bfs
对于每个坏掉的橘子 我们都需要扩散开 让它周围的橘子变成坏橘子
那么我们遍历上下左右
让每个坏掉的橘子 的上下左右 并且是新鲜橘子的话 那么我们就变成坏橘子
并且把它加入已经访问的set中
再加入进 new queue中
然后 当queue中的长度等于0 并且 new queue中有东西的时候 
我们时间才➕1 并且清空 new queue 因为 每分钟我们需要把所有当前坏橘子的周围变成坏橘子 但坏橘子有可能是多个 
所以queue真正的意义是 每分钟有几个坏橘子

'''