'''
用dp
首先初始化dp
然后状态转移方程
每个树 都是由左边 跟右边组成
然后左边有几种方法组成 乘 右边有几种方法组成 就直到 整个有几个方法组成了
 dp[i] += dp[j] * dp[i - j - 1] 意思是 左边是有j个方法组成 右边有i - j -1组成 为什么要-1 是因为root我们减去
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 卡特兰数
        if n <= 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                # 左边子树有 j个node 形成
                # 右边有 总数i - j - 1 个node 形成
                # -1 是因为 root需要一个node
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]

