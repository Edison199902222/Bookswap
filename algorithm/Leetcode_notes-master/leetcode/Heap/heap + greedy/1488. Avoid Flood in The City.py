class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        result = [-1] * n
        dic = collections.defaultdict(list)
        # 记录湖出现的位置
        for index, river in enumerate(rains):
            dic[river].append(index)
        # heap中的湖 都需要被清空
        heap = []

        for i in range(len(rains)):
            river = rains[i]
            if river > 0:
                # 说明之前没抽干，已经是满的了
                if dic[river][0] < i:
                    return []
                if len(dic[river]) >= 2:
                    heapq.heappush(heap, dic[river][1])

            else:
                # 遇到0 当前需要决定抽干哪一条湖
                if heap:
                    # 抽干离当前 0 后面 最近的一条湖， 越近的说明优先级越高（ 在heap中的每一个湖 都已经在之前出现了一次）
                    to_dry = heapq.heappop(heap)
                    result[i] = rains[to_dry]
                    # 并且 把dic中 抽干的湖给删掉一个index
                    dic[rains[to_dry]].pop(0)
                else:
                    result[i] = 1
        return result


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        heap = []
        # 因为要pop第一个，用deque 让复杂度变o1
        dic = collections.defaultdict(collections.deque)
        # 把所有要下雨的湖放进dic中
        for index, rain in enumerate(rains):
            if rain != 0:
                dic[rain].append(index)
        result = [1] * n
        for i in range(n):
            # 如果要下雨的话
            river = rains[i]
            if rains[i] != 0:
                # 如果之前满的湖没有清除的话，那么证明会溢出来
                if dic[river][0] < i:
                    return []
                # 如果下雨超过1次的话， 需要把下一次下雨日期放进heap中
                if len(dic[river]) >= 2:
                    heapq.heappush(heap, dic[river][1])
                result[i] = -1
            # 如果不下雨的话，决定抽哪一条河
            # 抽对于当前0来说，最近的并且之前已经出现过了
            # heap 中 的每一个河都表示已经在当前0之前出现过了，并且会出现2次以上
            # 所以 remove heap中顶部元素，这就是距离当前0 最近的河 并且需要 抽干的
            # heap 中所有的河index 都会在 当前0 idnex 之后，因为如果有一个在之前的话，会return 【】
            else:
                if heap:
                    to_dry = heapq.heappop(heap)
                    result[i] = rains[to_dry]
                    # 证明把这条河已经抽干
                    dic[rains[to_dry]].popleft()
        return result

