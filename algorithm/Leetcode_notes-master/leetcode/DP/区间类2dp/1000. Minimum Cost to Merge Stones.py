class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        self.memo = {}
        result = self.dfs(0, len(stones) - 1, 1, K, stones)
        return result if result != float("inf") else - 1

    # dp[i][j][m] 意思是 从数组 i 到j 合成m 堆，最小需要的代价
    def dfs(self, i, j, m, K, stones):
        # 如果 i == j的话，说明只有一块石头，如果要分成超过1 堆的话，肯定是分不成的
        if i == j:
            return 0 if m == 1 else float("inf")
        # 判断能不能最后剩下m堆石头
        # 原理是， [3, 2, 4, 1] m = 2， k = 3 时， 先拿走两个石头
        # 第一个石头放一边不管， 拿着另一个石头，然后看剩下的 n - m个石头 能不能凑成 k - 1 个， 每次都跟 手上的石头碰成1 一个
        # 每次如果都有k - 1 个时候和我手上的时候碰成1 个的话，最后就会剩下 第一个石头 + 上手上的一个石头
        if (j - i + 1 - m) % (K - 1):
            return float("inf")
        # 如果最后想要剩下1 堆石头的话， 只能看i 到 j 能不能变成k堆石头的最小代价 + 现在这么多堆石头成的代价
        if m == 1:
            return self.dfs(i, j, K, K, stones) + sum(stones[i: j + 1])

        if (i, j, m) in self.memo:
            return self.memo[(i, j, m)]
        # 找最后一堆石头的起始点
        result = float("inf")
        for mid in range(i, j):
            # 需要保证，i < j的
            # 找到最后一堆的起点之后，计算 i 到mid 合并成m - 1堆最小的cost 加上 mid +1 到j合并成1 堆最小的cost
            result = min(result, self.dfs(i, mid, m - 1, K, stones) + self.dfs(mid + 1, j, 1, K, stones))

        self.memo[(i, j, m)] = result
        return result

