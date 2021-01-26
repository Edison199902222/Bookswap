class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        result = []
        left = 0
        right = len(nums) - 1
        while left < right:
            sums = nums[left] + nums[right]
            if sums == target:
                result += [left + 1, right + 1]
                return result
            elif sums > target:
                right -= 1
            else:
                left += 1
'''
跟259 这些一样的
'''