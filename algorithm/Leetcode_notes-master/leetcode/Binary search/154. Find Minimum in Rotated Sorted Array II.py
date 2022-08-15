class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            target = nums[right]
            if nums[mid] > target:
                left = mid
            elif nums[mid] < target:
                right = mid
            else:
                right -= 1
        return min(nums[left], nums[right])
'''
跟153 很像，只是多了一个条件 就是存在重复的情况 
比如[3,3,1,3]这种情况下，如果我们还是用原来的算法
那么就找不到最小值1，所以我们发现 如果当 mid 跟 right 相等时，我们就找不到
所以 这种情况 要分开讨论，如果 mid 跟 right相等时，我们就无脑把right - 1， 这样我们就可以重新判断 最小值到底在哪个方向，
而且 如果 right 就是最小值的话，无脑- 1 也不会错过，因为我们mid 也是等于 right 的值
'''