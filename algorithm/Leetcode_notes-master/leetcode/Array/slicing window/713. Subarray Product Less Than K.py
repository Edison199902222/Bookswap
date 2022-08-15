class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        result = 0
        prefix_sum = 1
        left = 0
        for right in range(len(nums)):
            prefix_sum *= nums[right]
            while left < right and prefix_sum >= k:
                prefix_sum /= nums[left]
                left += 1
            if prefix_sum < k:
                # 必须带上当前值，算的所有subaray
                result += (right - left + 1)
        return result
