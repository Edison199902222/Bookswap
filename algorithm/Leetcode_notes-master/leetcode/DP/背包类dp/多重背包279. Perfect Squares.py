''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i]表示 数为i时，最少需要多少的perfect square number
        dp = [i for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:  # 多重背包问题 限制个数
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

'''
多重背包问题
内循环中有while 来判断 我们需要取多少个物品j
对比一下完全背包，其实只是多了一个限制条件，完全背包问题中，物品可以选择任意多件，只要你装得下，装多少件都行
但多重背包就不一样了，每种物品都有指定的数量限制，所以不是你想装，就能一直装的。
f[i][v]=max{f[i-1][v-k*c[i]]+k*w[i]|0<=k<=n[i]}
多重背包问题内含while 循环
'''

