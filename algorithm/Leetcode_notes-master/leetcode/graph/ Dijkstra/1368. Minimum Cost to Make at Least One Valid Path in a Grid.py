import heapq


class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        # 储存的是 cost，i， j
        heap = [(0, 0, 0)]
        # 记录cost, 如果发现有cost 低于 seen里面的，可以更新掉， 限制 cost 比 seen中大的点放进heap中
        seen = {}
        seen[(0,0)] = 0
        while heap:
            # 每一次走cost 最低的， 保证第一次走到终点时，cost最低
            cost, i, j = heapq.heappop(heap)
            if i == m -1 and j == n - 1:
                return cost
            for new_x, new_y, sign in [(i + 1, j, 3), (i - 1, j, 4), (i, j - 1, 2), (i, j + 1, 1)]:
                if sign == grid[i][j]:
                    new_cost = cost
                else:
                    new_cost = cost + 1
                if 0 <= new_x < m and 0 <= new_y < n and ( (new_x, new_y) not in seen or new_cost < seen[(new_x, new_y)]):
                    heapq.heappush(heap, (new_cost, new_x, new_y ))
                    seen[(new_x, new_y)] = new_cost
        return -1