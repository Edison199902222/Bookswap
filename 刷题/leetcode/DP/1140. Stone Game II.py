class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        presum = [0 for i in range(len(piles) + 1)]
        for i in range(len(piles)):
            presum[i + 1] = presum[i] + piles[i]
        self.memo = {}
        return self.dfs(presum, 1, 0)

    def dfs(self, presum, M, index):
        if index >= len(presum) - 1:
            return 0
        if len(presum) - 1 - index <= 2 * M:
            return presum[len(presum) - 1] - presum[index]
        if (index, M) in self.memo:
            return self.memo[(index, M)]
        result = 0
        for i in range(1, 2 * M + 1):
            cur = float("inf")
            for j in range(1, 2 * max(i, M) + 1):
                cur = min(cur, self.dfs(presum, max(j, max(i, M)), index + i + j))
            cur += presum[index + i] - presum[index]
            result = max(result, cur)
        # 同一个index 有不同的M 表示状态！！一定要记住
        self.memo[(index, M)] = result
        return result
