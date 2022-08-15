class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    def previousPermuation(self, nums):
        # write your code here
        index = len(nums) - 2
        while index > - 1:
            # 找到一个数，后面的数字比它小的
            if nums[index] > nums[index + 1]:
                j = pivot = index + 1
                # 找到最接近index的数，并且是小于index的
                while j < len(nums) and nums[index] > nums[j]:
                    pivot = j
                    j += 1
                # 交换位置
                nums[index], nums[pivot] = nums[pivot], nums[index]
                break
            index -= 1
        # 降序排序保证后面是最大的
        nums[index + 1:] = nums[index + 1:][::-1]
        return nums

