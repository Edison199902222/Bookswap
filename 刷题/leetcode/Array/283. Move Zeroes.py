'''
j指针只指向为0的数字 遇到不为0的数字 则跳过
i指针指向不为0的数字

'''


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        j = 0
        for i in range(1, len(nums)):
            if nums[j] == 0 and nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            if nums[j] != 0:
                j += 1
