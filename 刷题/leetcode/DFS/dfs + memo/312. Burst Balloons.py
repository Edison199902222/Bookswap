class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.memo = {}
        nums = [1] + nums + [1]
        return self.dfs(nums, 0, len(nums) - 1)
    def dfs(self, nums, left, right):
        if left == right:
            return 0
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        result = 0
        for k in range(left + 1, right):
            left_ones = self.dfs(nums, left, k)
            right_ones = self.dfs(nums, k, right)
            result = max(result, left_ones + right_ones + nums[left] * nums[k] * nums[right])
        self.memo[(left, right)] = result
        return result
'''
首先 需要在nums数组中 前后 加1 是因为，当我们刺第一个气球时， 需要前面有一个1 来得到比分
然后 dp[i][j]表示 打破 第i + 1 ～ 第j - 1 个气球时的最大价值， 留下 i跟j
base case 如果 left == right 证明中间没有气球了
我们遍历 left + 1 到right， 从中枚举 每一个气球作为我们最后要打爆的气球k
然后 dfs 搜索 左边left ～ k， 右边k ～ right， result 就会等于 左边部分 加上右边部分再加上 我们 打爆k的分数， 等于 left * k *right， 因为我们假设了 其他所有气球已经爆了
然后更新memo
'''