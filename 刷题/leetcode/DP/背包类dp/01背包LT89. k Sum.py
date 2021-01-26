class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """

    def kSum(self, A, k, target):
        # write your code here
        dp = [[[0] * (target + 1) for i in range(k + 1)] for i in range(len(A) + 1)]
        dp[0][0][0] = 1
        for i in range(1, len(A) + 1):
            dp[i % 2][0][0] = 1
            for j in range(1, k + 1):
                for x in range(1, target + 1):
                    dp[i % 2][j][x] = dp[(i - 1) % 2][j][x]
                    if x >= A[i - 1]:
                        dp[i % 2][j][x] += dp[(i - 1) % 2][j - 1][x - A[i - 1]]

        return dp[len(A) % 2][k][target]
'''
dp[i][j][k]代表 前i 个数 选择j个数 组成target这个数 有多少种方式
每一次我们可以选择， 如果当前枚举的target 这个数 大于我们现在的数，那么意味着 我们有两种选择
我们可以选择这个数， 或者不选择这个数
如果选的话  dp[i % 2][j][x] += dp[(i - 1) % 2][j - 1][x - A[i - 1]] 
意思是 当前的有多少种选法是依赖于 之前 组成 前i - 1 个物品 选择j - 1 个数 组成 target 减去 当前数 的方式有多少种， 因为之前的这种选法， 加上当前数就是我们要的target
或者 不选择  dp[i % 2][j][x] = dp[(i - 1) % 2][j][x]， 因为不选择当前的数，所以一定要在 前i -1个数中 选择j 个数 组成 x 
'''