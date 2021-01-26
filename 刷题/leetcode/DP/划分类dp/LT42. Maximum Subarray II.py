class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums or len(nums) == 1:
            return 0
        # 从前往后扫，得到截止index 左边的最大值 包括index
        # 从后往前扫，得到截止index 右边的最大值 包括idnex
        n = len(nums)
        prefix = 0
        dp_left = [0 for i in range(n)]
        local_min = 0
        global_max = float("-inf")
        for i in range(n):
            prefix += nums[i]
            # 得到当前最大值
            global_max = max(global_max, prefix - local_min)
            # 更新下一轮的local min
            local_min = min(local_min, prefix)
            dp_left[i] = global_max

        suffix = 0
        dp_right = [0 for i in range(n)]
        local_min = 0
        global_max = float("-inf")
        for i in range(n - 1, -1, -1):
            suffix += nums[i]
            global_max = max(global_max, suffix - local_min)
            local_min = min(local_min, suffix)
            dp_right[i] = global_max

        # 最后加起来
        result = float("-inf")
        for i in range(n - 1):
            result = max(result, dp_left[i] + dp_right[i + 1])
        return result

    class Solution:
        """
        @param: nums: A list of integers
        @return: An integer denotes the sum of max two non-overlapping subarrays
        """

        def maxTwoSubArrays(self, nums):
            # write your code here
            if not nums or len(nums) == 1:
                return 0
            n = len(nums)
            prefix = 0
            dp_left = [float("-inf") for i in range(n + 1)]
            local_min = 0
            for i in range(1, n + 1):
                prefix += nums[i - 1]
                dp_left[i] = max(dp_left[i - 1], prefix - local_min)
                local_min = min(local_min, prefix)

            suffix = 0
            local_min = 0
            result = float("-inf")
            for i in range(n - 1, 0, -1):
                suffix += nums[i]
                result = max(result, suffix - local_min + dp_left[i])
                local_min = min(local_min, suffix)
            return result
