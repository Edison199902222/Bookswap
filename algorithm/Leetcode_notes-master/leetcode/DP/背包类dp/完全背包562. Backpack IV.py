'''
比较naive的版本
dp[i][j]代表 前i 个物品 可以组成体积为j 的方式 有几种
初始化， dp[0][0]肯定是1， 组成0 体积的方式可以是一种，就是什么都不选
然后遍历我们的物品
枚举 体积， 只要体积可以装得下，那么我们就枚举k， 当它现在选0件 选1件 选两件的时候， 有几种可以组成它们的体积的方式 全部加起来
所以， 完全背包问题不再是选 或者不选，而是当前物品选几个
'''


class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        dp = [[0 for i in range(target + 1)] for i in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                k = 0
                while k * nums[i - 1] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i - 1] * k]
                    k += 1
        return dp[len(nums)][target]

'''
完全背包的优化
我们使用 只关注 当前不选择 跟 选择大于等于1 的情况
其实对于完全背包问题， 我们不需要 关注 前面i - 1 个物品的问题
因为对于当前的物品来说， 我们可能不选择 或者选N次， 在01背包问题时，我们为什么需要i -1 呢，是因为我们第i 个物品只能选择一次，不想重复选择
所以 在这个问题上
我们当前状态只有两种，一种是不选择，那么 前i 个物品 组成j体积的 是跟 前i - 1 个物品 组成j体积 的方式 一样的, 所以不需要更新！！！
如果选择的话， 我们就可以 推导 dp[i % 2][j] += dp[i % 2][j - nums[i - 1]] 意思是 前i 个物品 组成j 体积的 是由自身的 + 前i个物品 组成j - i 体积 的方式

'''
class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        dp = [0 for i in range(target + 1)]
        n = len(nums)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j >= nums[i -1]:
                    dp[j] += dp[j - nums[i - 1]] # 为什么是加等于呢， 是因为 对于每个大于 当前物品i 的j， 是有两种组成j的方式的
                    # 一种是 不取当前的物品 也就是dp[i - 1][j] 一种是取当前的物品也就是dp[i][j - nums[i - 1]]，如果只是等于的话
                    # 意思是 只有一种情况也就是取当前的物品， 放弃了 不取当前物品的情况
        return dp[target]
