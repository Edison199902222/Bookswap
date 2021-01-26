class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.nums[i + 1] = self.nums[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j + 1] - self.nums[i]
'''
维持一个数组
数组 比 原数组 多一个 
新数组 第i 位表示 旧数组0 ～ i - 1 的和
然后 sum range 其实就是 用 0 ～ j + 1 表示 从 0 ～ j的和 减去 0 ～ i-1 的和 就是i ～j的和了
'''
    # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)