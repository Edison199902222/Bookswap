class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        self.memo = {}
        return self.dfs(len(coins), amount, coins)
    def dfs(self, i, amount, coins):
        if amount == 0:
            return 1
        elif i <= 0:
            return 0
        if (i, amount) in self.memo:
            return self.memo[(i, amount)]
        result = 0
        if amount >= coins[i - 1]:
            result += self.dfs(i, amount - coins[i - 1], coins)
        result += self.dfs(i - 1, amount, coins)
        self.memo[(i, amount)] = result
        return result
'''
完全背包问题
dfs 解法
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[j] += dp[j - coins[i - 1]]
        return dp[amount]