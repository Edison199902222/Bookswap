class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # 意思是，从起点 到 第i个点的最短路径的cost 是多少
        record = [float("inf") for i in range(N)]
        record[K - 1] = 0
        # 模版
        for i in range(N):
            # 每个edge 都走一次
            for e in times:
                # 每个edge 都更新一次
                record[e[1] - 1] = min(record[e[1] - 1], record[e[0] - 1] + e[2])

        return max(record) if max(record) != float("inf") else - 1
