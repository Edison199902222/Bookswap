import collections
import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(set)
        # 创建图
        for start, end, cost in flights:
            graph[start].add((end, cost))
        heap = []
        # Dijkstra 算法， 每次走cost最小的，去更新
        # 所以 cost放前面
        for next_stop, cost in graph[src]:
            heapq.heappush(heap, (cost, next_stop, 0))
        while heap:
            cost, cur_stop, level = heapq.heappop(heap)
            if level > K:
                continue
            if cur_stop == dst:
                return cost
            for next_stop, next_cost in graph[cur_stop]:
                heapq.heappush(heap, (cost + next_cost, next_stop, level + 1))
        return - 1