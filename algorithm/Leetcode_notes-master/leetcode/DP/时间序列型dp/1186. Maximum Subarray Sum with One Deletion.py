class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        # 0 代表未使用delete 以当前元素结尾最大和
        # 1 代表使用delete 以当前元素结尾最大和
        dp = [[float("-inf")] * 2 for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0] + arr[i - 1], arr[i - 1])
            dp[i][1] = max(dp[i - 1][1] + arr[i - 1], dp[i - 1][0])

        result = float("-inf")
        for i in range(1, n + 1):
            result = max(result, dp[i][0], dp[i][1])

        return result