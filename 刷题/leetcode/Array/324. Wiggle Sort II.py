class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        if n < 2:
            return
        num = [0 for i in range(len(nums))]
        index = n - 1
        for i in range(1, n, 2):
            num[i] = nums[index]
            index -= 1
        for i in range(0, n, 2):
            num[i] = nums[index]
            index -= 1
        for i in range(n):
            nums[i] = num[i]
        return
'''
暴力法
'''