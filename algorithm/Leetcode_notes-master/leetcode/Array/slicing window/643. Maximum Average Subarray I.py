class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0
        left = 0
        sums = 0
        result = float("-inf")
        for right in range(len(nums)):
            sums += nums[right]
            if right - left + 1 == k:
                result = max(result, sums/k)
                sums -= nums[left]
                left += 1
        return result
'''
滑动窗口模版题

'''