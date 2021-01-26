class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        dp = [0 for i in range(m + 1)]
        n = len(A)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[j] = max(dp[j], dp[j - A[i - 1]] + V[i - 1])
        return dp[m]
'''
完全背包问题
内循环从里往外遍历
跟01 背包不一样的是 在01背包问题时，我们为什么需要i -1 呢，是因为我们第i 个物品只能选择一次，不想重复选择。
我们对于第i个物品来说， 我们不需要再依靠i - 1
'''


class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    def backPackIII(self, A, V, m):
        # write your code here
        dp = [[0 for i in range(m + 1)] for i in range(len(A) + 1)]
        n = len(A)
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                k = 0
                while k * A[i - 1] <= j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k * A[i - 1]] + k * V[i - 1])
                    k += 1

        return dp[n][m]
'''
优化前
'''