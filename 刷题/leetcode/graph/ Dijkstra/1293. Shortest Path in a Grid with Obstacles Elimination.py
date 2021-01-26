class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        heapq.heappush(heap, (0, 0, 0, k))
        m = len(grid)
        n = len(grid[0])
        seen = {}
        # 有可能反复访问同一个点，但每一次访问的k是不一样，所以记录k， 如果当前去的k 还大于之前的，那么没有必要再去
        # 如果小于的话，可以再去一次
        seen[(0,0)] = k
        while heap:
            steps, i, j, cost = heapq.heappop(heap)
            if i == m - 1 and j == n - 1:
                if cost >= 0:
                    return steps
                else:
                    continue
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and ((x, y) not in seen or cost > seen[(x,y)]):
                    if grid[x][y] == 1:
                        if cost >= 0:
                            seen[(x,y)] = cost - 1
                            heapq.heappush(heap, (steps + 1, x, y, cost - 1))
                    else:
                        heapq.heappush(heap, (steps + 1, x, y, cost))
                        seen[(x,y)] = cost
        return -1


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = collections.deque()
        queue.append((0, 0, 0, 0))
        m = len(grid)
        n = len(grid[0])
        # 有可能反复访问同一个点，但每一次访问的k是不一样，所以记录k， 如果当前去的k 还大于之前的，那么没有必要再去
        # 如果小于的话，可以再去一次
        seen = collections.defaultdict(int)
        seen[(0,0)] = 0
        while queue:
            steps, cost, i, j = queue.popleft()
            if i == m - 1 and j == n - 1:
                return steps
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 1 and cost + 1 <= k and ((x, y) not in seen or cost + 1 < seen[(x,y)]):
                            queue.append((steps + 1, cost + 1, x, y))
                            seen[(x,y)] = cost + 1
                    elif grid[x][y] == 0 and ((x, y) not in seen or cost < seen[(x,y)]):
                        queue.append((steps + 1, cost, x, y))
                        seen[(x,y)] = cost
        return - 1