'''
用二分法 时间复杂度是nlogn
每一次 假设 数组长度是n
我们每一次取 1 到 n - 1范围的数
所以 一共有n - 1 个number 但是我们需要n个数，所以一定会有一个数字重复
我们观察得到，假设现在有 1 2 3 3 4， 我们假设mid 是2，那么我们搜索数组，发现小于等于2的数 的数量等于2
如果mid 是3， 我们搜索数组，发现小于等于3 的数 的数量是4
所以我们知道， 如果当前的mid 不是重复的数字的话，那么小于等于mid 的数量一定是小于等于mid 的值
如果mid 是重复的数字的话，那么小于等于mid的数量一定大于mid的值

所以我们使用二分法 left = 1， right = n - 1 因为 n-1是最大能取的值
每一次查找小于等于mid 的数量，如果大于mid的值 说明， 重复的值在我们左边
如果小于等于mid的值，说明当前数字不是重复的数字，重复的值在我们右边
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return
        left = 1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.caculate(nums, mid) > mid:
                right = mid
            else:
                left = mid
        if self.caculate(nums, left) > left:
            return left
        return right

    # caculate how many numbers is less or equen to value
    def caculate(self, nums, value):
        count = 0
        for i in nums:
            if value >= i:
                count += 1
        return count

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while(slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while(fast != slow):
            slow = nums[slow]
            fast = nums[fast]
        return slow


