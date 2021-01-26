class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [[False for i in range(m + 1)] for i in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        for i in range(m, -1, -1):
            if dp[n][i]:
                return i
        return 0
'''
dp[i][j]表示 前i 个物品能够组成 j 体积 是否存在
每一次 我们可以选背上当前物品 或者不背
遍历数组
初始化 0 0， 10， 2 0，为true 因为 前i个东西 肯定可以组成体积为0 的背包，就是什么都不选
然后遍历数组， 枚举体积的所有可能性
如果当前枚举体积 是大于等于当前拾取背包的体积， 
那么dp[i][j] 就会依赖于 前i - 1 个物品能组成j 体积 是否存在 或者 依赖于 前i - 1个物品 是否存在可以组成 体积j - 当前拾取背包的体积
如果 当前枚举的体积 小于我们当前背包的体积 那么 它不可能依赖于 前i - 1 个物品 组成j - 当前背包的体积， 因为这样 组成的体积会变成负数
它依赖于 前i - 1 个物品 组成j体积 是否存在
'''


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)
        f = [[False] * (m + 1), [False] * (m + 1)]

        f[0][0] = True
        for i in range(1, n + 1):
            f[i % 2][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i % 2][j] = f[(i - 1) % 2][j] or f[(i - 1) % 2][j - A[i - 1]]
                else:
                    f[i % 2][j] = f[(i - 1) % 2][j]

        for i in range(m, -1, -1):
            if f[n % 2][i]:
                return i
        return 0
'''
因为我们 每个i 的状态 只跟之前 的i的状态有关， 所以我们可以使用滚动数组来进行优化
'''
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [0 for i in range(m + 1)]
        for i in range(1, n + 1):
            for j in range(m, -1, -1):
                if j >= A[i - 1]:
                    dp[j] = max(dp[j], dp[j - A[i - 1]] + A[i - 1])
        return dp[m]