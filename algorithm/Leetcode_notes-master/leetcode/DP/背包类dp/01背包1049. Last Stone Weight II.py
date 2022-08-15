class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        sums = sum(stones) // 2
        dp = [0 for i in range(sums + 1)] # 表示前i个石头 背包体积为j 最多能装多少value 的石头
        for i in range(len(stones)):
            for j in range(sums, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        return sum(stones) - 2*dp[sums]

'''
这是优化后的01 背包
内层循环从大到小
我们需要找到两堆 石头 这两堆石头的大小越接近越好
所以 我们用sum // 2 当背包的体积由于 我们是向下取整，所以找出来的肯定是较小的那一堆石头
去数组中 寻找一堆接近我们体积的一堆石头
用背包dp 寻找完之后， 
我们用sum - 这堆石头 就是另一堆石头可以组成value
然后 两堆石头相减 就是最终的答案
'''

