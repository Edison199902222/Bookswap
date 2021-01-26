class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[float("-inf")] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dot = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(dp[i][j], dot, dp[i - 1][j - 1] + dot, dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
'''
dp[i][j] = max(dp[i][j], dot, dp[i - 1][j - 1] + dot, max(dp[i][j - 1], dp[i - 1][j]))
对于现在的max dot和，我们需要依靠 
首先要考虑 之前全是负数， 但现在第 i 跟 第j 个元素 相乘是正数的情况， 所以有可能把前面的全丢掉，只要自己这部分的乘积和 也就是dot = nums1[i - 1] * nums2[j - 1]
然后就是自身的
然后 如果前面是正数的话，那么加上我们 dot 也可能更大 所以也要考虑 dp[i - 1][j - 1] + dot
还要考虑 之前的和  dp[i][j - 1], dp[i - 1][j]
'''