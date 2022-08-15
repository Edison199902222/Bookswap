class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # 0 表示 以i元素结尾，未使用过flip 的最长连续1
        # 1 表示 以i元素结尾，使用过flip 的最长连续1
        dp = [[0] * 2 for i in range(n + 1)]
        for i in range(1, n + 1):
            if nums[i - 1] == 0:
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1] + 1

        max_result = 0
        # 因为每一个结尾的位置都不一样，每个位置都有可能是最大的
        for i in range(1, n + 1):
            max_result = max(max_result, dp[i][0], dp[i][1])
        return max_result

    class Solution(object):
        def findMaxConsecutiveOnes(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            # 储存上一次0 之前的长度
            prev = - 1
            cur = 0
            result = 0
            for num in nums:
                # 遇到0的话，把cur 设置为0， 表示重新开始计算
                # 并且把 cur 赋给prev
                if num == 0:
                    prev, cur = cur, 0
                else:
                    # 直接 加 1
                    cur += 1
                # 没遇到0的话，只加cur
                # 遇到0的话，前一个长度 + 1（翻转） 再加上现在的长度
                result = max(result, prev + 1 + cur)
            return result
