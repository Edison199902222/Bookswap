'''
两种方法 第一种， 用排序
排序后 我们从数组第三位开始，每隔两个与之前的一个数字进行交换
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(0, len(nums) - 1, nums)
        for i in range(2, len(nums), 2):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return nums

    def partition(self, left, right, nums):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def quicksort(self, left, right, nums):
        if left < right:
            pos = self.partition(left, right, nums)
            self.quicksort(left, pos - 1, nums)
            self.quicksort(pos + 1, right, nums)
'''
使用第二种方法
我们遍历数组
对于每一位来说 如果它的index 是奇数的话，就需要大于前面的一位数
如果是偶数的话 就需要 小于前面一位数
我们用一个 bool 去判断需不需要 交换
如果当前元素不满足 所对应的条件的话，我们就让这一位 跟之前的一位进行交换
'''


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        for i in range(1, len(nums)):
            if i % 2:
                should_swap = nums[i] < nums[i - 1]
            else:
                should_swap = nums[i] > nums[i - 1]
            if should_swap:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return nums
        # 看单调性
        # 用flag 标记 当前的单调性，如果flag 为 true 必须现在elment 比 前一个大，如果比前一个小，那么交换
        # flag 为 false 必须现在element 比前一个小 如果当前element 比前一个大，那么交换
        # 现在elment 大于 前一个element，现在需要递减，前面是递增的，那么跟前面交换element以后，前面element变得更大
        # 所以并不会影响前面已经拍好的顺序
        flag = True
        for i in range(1, len(nums)):
            if flag:
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                flag = False
            else:
                if nums[i] > nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                flag = True

