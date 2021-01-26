import collections


class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(points) < 2:
            return 0
        # yi + yj + |xi - xj| = yi + yj + (xj - xi) = (yi - xi) + (xj + yj)
        # 因为 x是按顺序排列的，xj 肯定比 xi大，所以绝对值可以去掉
        heap = []
        # 储存(yj - xj), xj
        heapq.heappush(heap, (-(points[0][1] - points[0][0]), points[0][0]))
        result = float("-inf")
        for i in range(1, len(points)):
            # 发现不合法的点，直接pop
            while heap and points[i][0] - heap[0][1] > k:
                heapq.heappop(heap)
            if heap:
                result = max(result, -heap[0][0] + points[i][0] + points[i][1])
            heapq.heappush(heap, (-(points[i][1] - points[i][0]), points[i][0]))
        return result


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # yi + yj + |xi - xj| = yi + yj + (xj - xi) = (yi - xi) + (xj + yj)
        # 因为 x是按顺序排列的，xj 肯定比 xi大，所以绝对值可以去掉
        # 维护递减， 储存[yi - xi, xi]
        queue = collections.deque()
        result = float("-inf")
        for x, y in points:
            while queue and x - queue[0][1] > k:
                queue.popleft()
            if queue:
                result = max(result, queue[0][0] + x + y)
            # 把当前y - x 放进去, 小于当前y - x的话，pop出去
            while queue and queue[-1][0] <= y - x:
                queue.pop()
            queue.append((y - x, x))
        return result