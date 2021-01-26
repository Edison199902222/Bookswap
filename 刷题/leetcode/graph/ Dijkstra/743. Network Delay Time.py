class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 建立图
        for start, end, time in times:
            graph[start].append((end, time))
        heap = []
        # 把起始点 放进heap
        for end, time in graph[K]:
            heapq.heappush(heap, (time, end))
        # 记录走过的节点，与它最小的cost
        dic = {}
        dic[K] = 0
        while heap:
            cost, cur = heapq.heappop(heap)
            # 如果没有走过, 防止之后再更新， 保证最低cost
            if cur not in dic:
                dic[cur] = cost
                for end, new_cost in graph[cur]:
                    heapq.heappush(heap, (cost + new_cost, end))
        return max(dic.values()) if len(dic) == N else - 1


'''
时间复杂度： 需要遍历图的每个边 复杂度是O(E) 还要遍历整个heap 的大小 并且 要把 所有的V 加入进heap中， 应该是O(V*logV）
所以是 O(vlogv + elogv) = (v + e) logv
空间复杂度： 字典大小是 O(E) + 另一个存node 字典的大小 O(V)
O（E + V）
'''