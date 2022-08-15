class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][m]

'''
dp[i][j]表示 前i个物品 能组成 j 体积的 最大价值
每一次 我们可以选择 把当前物品加入进来， 或者不加入当前物品
那么枚举物品 
枚举 体积， 如果当前枚举的体积 大于 当前物品的体积的话， 那么我们可以选择当前的物品，我们可以得到 现在前i 个物品 构成j 体积 的最大价值是取决于
前i -1 个物品构成的j体积的最大价值，或者 前 i -1 个物品构成 （j - 当前物品的体积）的最大价值 加上 当前物品的价值
如果 枚举的体积 小于当前物品的体积的话，那么我们无法把物品带上，因为超过我们当前背包的最大体积了。 所以它的最大价值取决于 前i -1 个物品构成 j体积的最大价值
'''

'''
因为我们发现 dp【i】【j】只跟dp【i-1】有关
利用滚动数组优化
'''


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        dp = [0 for i in range(m + 1)]
        for i in range(1, n + 1):
            for j in range(m, -1, -1):
                if j >= A[i - 1]:
                    dp[j] = max(dp[j], dp[j - A[i - 1]] + V[i - 1])
        return dp[m]

