class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        k_sum = [sum(nums[:k])]
        n = len(nums)
        for i in range(1, n - k + 1):
            # 计算每k个subarray 的和
            k_sum.append(k_sum[-1] - nums[i - 1] + nums[i + k - 1])
        # 计算当前index i 左边最大的subarray 有多大
        dp_left = [0 for i in range(n)]
        max_val = float("-inf")
        max_index = 0
        for i in range(n - k + 1):
            if k_sum[i] > max_val:
                max_val = k_sum[i]
                max_index = i
            dp_left[i] = max_index

        dp_right = [0 for i in range(n)]
        max_val = float("-inf")
        for i in range(n - k, -1, -1):
            # 因为想要lexicographically smallest one， 从右往左的过程中， 同样的sum的情况下 index 越小越好
            if k_sum[i] >= max_val:
                max_val = k_sum[i]
                max_index = i
            dp_right[i] = max_index
        max_sum = float("-inf")
        result = []
        # 枚举 中间subarray 可以取的start， 最多只能取到 后面要留两个k， 一个k 给自己，一个k留给最后一个区间
        for i in range(k, n - 2 * k + 1):
            if k_sum[i] + k_sum[dp_left[i - k]] + k_sum[dp_right[i + k]] > max_sum:
                result = [dp_left[i - k], i, dp_right[i + k]]
                max_sum = k_sum[i] + k_sum[dp_left[i - k]] + k_sum[dp_right[i + k]]
        return result


