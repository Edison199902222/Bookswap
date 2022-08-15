class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums)
        for index, val in enumerate(nums):
            right -= val
            if left == right:
                return index
            left += val
        return - 1
'''
一个巧妙的方法
把left 设置为0 因为第一个数字的左边的和是0
然后把right 先设置为整个数组的和
然后 遍历数组
当第一个数字来的时候
先把right减去第一个数字 这就是此时第一个数字右边的和
然后比较左右相不相等
判断完后 把左边加上第一个数字 
'''