class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
        n = len(nums)
        # dp[i][j] 到i为止， 切成 k 个subarray， 的最大值
        # local 是必须带上i 的最大值
        # global 是不一定带上i的最大值
        local_max = [[0] * (k + 1) for i in range(n + 1)]
        global_max = [[0] * (k + 1) for i in range(n + 1)]
        for i in range(1, n + 1):
            # 取最小值，是因为如果k 超过当前 数组的数量i，比如 截止到i 数组中有三个元素，却要分成4 个subarray
            # 这是没有办法分的
            for j in range(1, min(i, k) + 1):
                # global[i-1][j-1]表示nums[i]重新开始一个新的子数组
                #  第 i 个元素贪心地选择自己加入第 j-1 组还是自己成为独立第 j 组
                # # local[i-1][j]表示nums[i]加入上一个子数组成为一部分
                    # global[i-1][j-1]表示nums[i]重新开始一个新的子数组
                if i == j:
                    # 当前i个数组要切成i个subarray时，就必须要带上第i个元素
                    # 所有的数组都必须单独成队， 所以local[i] 只会被 local[i - 1]更新
                    local_max[i][j] = local_max[i - 1][j - 1] + nums[i - 1]
                    global_max[i][j] = local_max[i][j]
                else:
                    # 在不需要所有数组单独成队的情况下，当前的local[i] 可以由两种选择
                    # 一种是当前的数字i 自己单独成一个subarray，跟global_max[i - 1][j - 1] 组成
                    # 一种是当前数字i 加入 local_max[i - 1][j】
                    local_max[i][j] = max(local_max[i - 1][j], global_max[i - 1][j - 1]) + nums[i - 1]
                    global_max[i][j] = max(global_max[i - 1][j], local_max[i][j])
        print(local_max)
        return global_max[n][k]
