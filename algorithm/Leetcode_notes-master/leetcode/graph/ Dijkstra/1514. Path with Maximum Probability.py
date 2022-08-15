class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # 最大堆， 因为要走概率大的
        heap = []
        graph = collections.defaultdict(set)
        i = 0
        # 创立图
        for begin, stop in edges:
            graph[begin].add((stop, succProb[i]))
            graph[stop].add((begin, succProb[i]))
            i += 1
        # 如果end 走不到，直接return 0
        if len(graph[end]) == 0:
            return 0
        # 把start 的下一站放进heap中
        for next_stop, cost in graph[start]:
            heapq.heappush(heap, (-cost, next_stop))
        # dic 记录 每个点 对应 的最大的概率
        dic = collections.defaultdict(int)
        dic[start] = 1
        # 用来保存走过的节点
        seen = set()
        while heap:
            # 每次走一个
            cost, cur_stop = heapq.heappop(heap)
            # 走过的节点不应该再走了，dijk的思想
            if cur_stop in seen:
                continue
            # 把走过的节点放进seen中
            seen.add(cur_stop)
            dic[cur_stop] = -cost
            # 如果找到了
            if cur_stop == end:
                return -cost
            for neighbor, new_cost in graph[cur_stop]:
                # 如果已经visited了 并且现在走到的概率 不如 之前走的，就选择不走
                if neighbor in dic and (-cost) * new_cost <= dic[neighbor]:
                    continue
                # 把当前neighbor 对应的概率 记录进去
                dic[neighbor] = -cost * new_cost
                heapq.heappush(heap, (cost * new_cost, neighbor))
        return 0

'''
时间复杂度 O(vlogv + Elogv) => (V + E) logV
'''