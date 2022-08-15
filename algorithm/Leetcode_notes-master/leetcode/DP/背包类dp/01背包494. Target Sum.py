class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.memo = {}
        sums = sum(nums)
        if sums < S:
            return 0
        return self.dfs(len(nums) - 1, S, nums, sums)

    def dfs(self, index, k, nums, sums):
        if index <= -1 and k == 0:
            return 1

        if index <= -1:
            return 0

        if (index, k) in self.memo:
            return self.memo[(index, k)]
        result = 0
        # 加上index
        if k - nums[index] >= -sums:
            result += self.dfs(index - 1, k - nums[index], nums, sums)
        # 减去 index
        if k + nums[index] <= 2 * sums:
            result += self.dfs(index - 1, k + nums[index], nums, sums)

        self.memo[(index, k)] = result
        return result
'''
元素和是nums_sum，整个数组的元素取值范围就是[-nums_sum,+nums_sum]，所以总共可能有的状态值就是2*nums_sum+1
        因为列表下标都是正的，所以设定一个offset，
        如[1,1,1,1,1]，取值范围是[-5,-4,-3,-2,-1,0,1,2,3,4,5]，那么0那个位置的下标其实是5，所以offset=nums_sum
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_nums = sum(nums)
        if sum_nums < S:
            return 0
        offset = sum_nums
        n = len(nums)
        dp = [[0 for i in range(2 * sum_nums + 1)] for i in range(n + 1)]
        dp[0][offset] = 1  # 初始化， 前0 个物品 组成target 为0 的也就1， 不需要取任何数
        for i in range(1, n + 1):
            for j in range(2 * sum_nums + 1):
                if j + nums[i - 1] < 2 * sum_nums + 1:  # 选择减去当前的nums[i]那么就要由上一行的 j + nums[i] 减去当前nums[i]得到
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # 选择加上当前nums[i] 就要由上一行的 j - nums[i] 加上当前nums[i]
        return dp[n][S + offset]
