class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return
        m = len(arr)
        n = len(arr[0])
        # dp[i][j] 代表第i行 第j列 最小path sum
        dp = [[0] * n for i in range(m + 1)]

        for i in range(1, m + 1):
            min_1 = min_2 = -1
            # 找出上一行最小值， 跟次小值
            for j in range(n):
                if min_1 == -1 or dp[i - 1][j] < dp[i - 1][min_1]:
                    min_2 = min_1
                    min_1 = j
                elif dp[i - 1][j] < dp[i - 1][min_2]:
                    min_2 = j
            for j in range(n):
                if j != min_1:
                    dp[i][j] = dp[i - 1][min_1] + arr[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][min_2] + arr[i - 1][j]
        result = float("inf")
        for i in range(n):
            result = min(result, dp[m][i])

        return result
