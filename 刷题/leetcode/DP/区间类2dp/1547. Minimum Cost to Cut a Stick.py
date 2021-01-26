class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        self.memo = {}
        return self.dfs(0, n, cuts)

    def dfs(self, start, end, cuts):
        # base case
        if start >= end:
            return 0
        if (start, end) in self.memo:
            return self.memo[(start, end)]
            # 对于从start 到end 区间内，如果cut在当前的区间内可以切割
        # 我们就尝试去切割每一个 可以切的木头， 更新最小的cost
        cost = float("inf")
        for i in range(len(cuts)):
            if cuts[i] >= end or cuts[i] <= start:
                continue
            cost = min(cost, (end - start) + self.dfs(start, cuts[i], cuts) + self.dfs(cuts[i], end, cuts))
        # 最后要判断，如果当前区间没有可以切割的木头，cost 要为0
        if cost == float("inf"):
            cost = 0
        self.memo[(start, end)] = cost
        return cost
