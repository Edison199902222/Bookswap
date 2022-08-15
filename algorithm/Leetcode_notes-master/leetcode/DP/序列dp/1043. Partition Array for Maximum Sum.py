class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        dp = [0] * n
        curmax = 0
        for i in range(len(A)):
            if i < K:
                curmax = max(curmax, A[i])
                dp[i] = curmax * (i + 1)
            else:
                curmax = 0
                for j in range(1, K + 1):
                    curmax = max(curmax, A[i - j + 1])
                    dp[i] = max(dp[i], dp[i - j] + curmax * j)
        return dp[n - 1]
'''
O(nk)
dp[i]表示 目前截止到数组的index i个 的最大值是多少
用curmax 去表示 数组到现在的最大值
循环遍历数组
如果当前index 小于k的话
那么我们的dp[i]其实就是依赖 当前最大值乘以 当前的长度

如果大于等于k的话 我们就可以尝试枚举长度 从1 到k  把最后 j 位给拆出来
那么 curmax 已经不是到目前为止的最大值了， 而是当前拆出来数组中的最大值， 
所以 dp[i] = max(dp[i], dp[i - j] + curmax * j)
拆出来的长度 乘 拆掉数组的最大值 加上 之前数组的最大值
'''