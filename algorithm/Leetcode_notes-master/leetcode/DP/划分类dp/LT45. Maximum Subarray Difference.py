class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """

    def maxDiffSubArrays(self, nums):
        # write your code here
        n = len(nums)
        left_min = [0 for i in range(n)]
        left_max = [0 for i in range(n)]
        right_min = [0 for i in range(n)]
        right_max = [0 for i in range(n)]
        prefix = 0
        local_min = 0
        local_max = 0
        global_min = float("inf")
        global_max = float("-inf")
        for i in range(len(nums)):
            prefix += nums[i]
            global_min = min(global_min, prefix - local_max)
            global_max = max(global_max, prefix - local_min)
            local_min = min(local_min, prefix)
            local_max = max(local_max, prefix)
            left_min[i] = global_min
            left_max[i] = global_max

        prefix = 0
        local_min = 0
        local_max = 0
        global_min = float("inf")
        global_max = float("-inf")
        for i in range(n - 1, -1, -1):
            prefix += nums[i]
            global_min = min(global_min, prefix - local_max)
            global_max = max(global_max, prefix - local_min)
            local_min = min(local_min, prefix)
            local_max = max(local_max, prefix)
            right_min[i] = global_min
            right_max[i] = global_max
        result = 0
        for i in range(1, n):
            result = max(result, abs(left_max[i - 1] - right_min[i]), abs(left_min[i - 1] - right_max[i]))
        return result

