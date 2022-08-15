class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0 or i == len(nums) - 1:
                result = max(result, count)
                count = 0
        return result
'''
遇到1 count 就 加1 
遇到其他的数字 或者当前数字 是数组最后一位了 那么我们就需要更新result 并且把count 清0
'''