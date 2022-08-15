class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        # 找到第一个大于等于x 的数
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < x:
                left = mid
            else:
                right = mid
        if nums[left] >= x:
            index = left
        elif nums[right] >= x:
            index = right
        else:
            index = len(nums)
        if index == len(nums):
            return nums[len(nums) - k:]
        # 然后找到一个大区间
        left = max(0, index - k)
        right = min(len(nums) - 1, index + k)
        # 逐渐缩小区间， 从2k 到 k
        while right - left + 1 > k:
            # 只有右边的跟x的差 小于 左边跟x的差，左边才移动
            if x - nums[left] > nums[right] - x:
                left += 1
            else:
                right -= 1
        return nums[left: right + 1]
