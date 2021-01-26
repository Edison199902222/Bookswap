class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 1
        n = min(n, 10)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 9
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (10 - (i - 1))
        return sum(dp)
'''
果n = 1，那么可以有10个数字不同（0～9）
如果n >= 2，那么第一位可以是1～9共9个数字，第二位可以是出去第一位的数字+0共9个数字，
之后的每位数字都必须不能使用前面已经用过的数字所以依次递减。
设dp[i]表示i位数时满足题意的数的个数。
对于第i位，为了使得第i位与前i-1位的数字不一致，我们可以选择数字应该有10-(i-1)个，因此转移方程为：dp[i]=dp[i-1]*(11-i)dp[i]=dp[i−1]∗(11−i)
'''