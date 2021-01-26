class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 代表持有
        # 1 清空
        # 2 清空一天以上
        if not prices:
            return 0
        dp = [[float("-inf")] * 3 for i in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        n = len(prices)
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[n - 1][1], dp[n - 1][2])