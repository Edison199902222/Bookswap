class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # max[i]表示 以index i 为结尾的最大乘积
        max_nums = nums[:]
        # min[i]表示 以index i 为结尾的最小乘积
        min_nums = nums[:]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                max_nums[i] = max(max_nums[i], max_nums[i - 1] * nums[i])
                min_nums[i] = min(min_nums[i], min_nums[i - 1] * nums[i])
            else:
                max_nums[i] = max(max_nums[i], min_nums[i - 1] * nums[i])
                min_nums[i] = min(min_nums[i], max_nums[i - 1] * nums[i])
        return max(max_nums)
'''
比较容易想出来的线性dp。由于数据中有正有负，所以我们利用两个dp数组来完成。用fi来保存计算到第i个时的最大值，用gi来保持计算到第i个时的最小值。
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        # 如果当前数小于0，那么有可能反转 因为 是负数， 所以要保留当前index 的最小值和最大值的subarray，
        # dp[i] 必须要带上i， 这就local 可以推出 global
        dp_max = [float("-inf") for i in range(n + 1)]
        dp_min = [float("inf") for i in range(n + 1)]
        dp_max[1] = nums[0]
        dp_min[1] = nums[0]
        for i in range(2, n + 1):
            # 如果小于0
            if nums[i - 1] < 0:
                # max 有可能由最小值转化，或者抛弃前面的只考虑当前数
                dp_max[i] = max(nums[i - 1], dp_min[i - 1] * nums[i - 1])
                # min 有可能由最大值转化
                dp_min[i] = min(nums[i - 1], dp_max[i - 1] * nums[i - 1])
            else:
                dp_max[i] = max(nums[i - 1], dp_max[i - 1] * nums[i - 1])
                dp_min[i] = min(nums[i - 1], dp_min[i - 1] * nums[i - 1])
        return max(dp_max)


