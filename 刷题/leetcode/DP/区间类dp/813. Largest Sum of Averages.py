class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        m = len(A)
        # dp[i][k] 表示前i个元素， 可以分成k个区间的Largest Sum of Averages
        dp = [[float("-inf")] * (K + 1) for i in range(m + 1)]
        dp[0][0] = 0

        for i in range(1, m + 1):
            for k in range(1, min(i, K) + 1):
                # 找寻最后一个区间开始的位置, 最多只能去到k，因为要保证前面的元素能够分成k - 1 个区间
                # 比如 k = 4， 开始的位置最多只能到4，保证前面3 个元素 能分成3 个区间，如果只有2 个元素 分不成3 个区间
                sums = 0
                for j in range(i, k - 1, - 1):
                    # 从后往前找，方便找sums
                    sums += A[j - 1]
                    dp[i][k] = max(dp[i][k], dp[j - 1][k - 1] + sums / (i - j + 1))

        result = float("-inf")
        for i in range(1, K + 1):
            result = max(result, dp[m][i])
        return result