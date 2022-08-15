class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return 0
        N = len(nums)
        dp = [1] * N
        for i, num in enumerate(nums):
            maxLen = 1
            for j in range(i):
                if num > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] == 3:
                        return True
        return False


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 跟300 一样的思路
        result = [float("inf") for i in range(len(nums))]
        index = -1
        for i in range(len(nums)):
            pos = self.binary_search(result, nums[i])
            if pos < len(nums):
                result[pos] = nums[i]
                if pos + 1 >= 3:
                    return True
        return False

    def binary_search(self, nums, value):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= value:
                right = mid
            else:
                left = mid
        if nums[left] >= value:
            return left
        if nums[right] >= value:
            return right
        return len(nums)