'''
因为这是个旋转排序数组，所以第一个小于最右边的值，一定是最小值
而找到这个最小值的方法就是利用二分法，把最右边的值设成target
设置一个target 使用target记录数组最右端的数字
如果mid 大于 target的话 区间向右边移动
如果 小于 target 区间向左移动
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        target = nums[len(nums) - 1]
        while left + 1 < right:
            mid = left + (right - left)/2
            if nums[mid] <= target:
                right = mid
            elif nums[mid] > target:
                left = mid
        return min(nums[left],nums[right])
'''
第二种解法
每次跟end 比较 
[3,4,5,1,2]  当left 为 3 right 为2 的时候
中间值是 5， 我们用5 跟2 比较， 5 比 2 大， 说明 5 这个位置是被旋转后的，左边肯定不存在最小值，所以区间向右移动
[4,5,6,7,0,1,2] 当left 为0 的时候 right 为 2 
中间值是 1， 我们发现 1 小于2， 说明现在这个区间 没有旋转， 找的最大值一定在左边 区间向左移动
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # 通过跟尾部比较 来确定区间
        while left + 1 < right:
            mid = (left + right) // 2
            # 如果mid 大于 尾部元素，说明我们处于旋转中，正常的话，mid 不可能大于right的
            # 所以，后半部分被旋转了， 现在的后半部分 其实就是 正常的前半部分，所以 最小值在右边
            if nums[mid] > nums[right]:
                left = mid
            # 如果mid 小于尾部元素，满足单调性，最小值在左边
            else:
                right = mid
        if nums[left] <= nums[right]:
            return nums[left]
        return nums[right]