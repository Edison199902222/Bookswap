class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        result = 1
        for right in range(1, len(nums)):
            if nums[right] <= nums[right - 1]:
                left = right
            result = max(result, right - left + 1)
        return result
