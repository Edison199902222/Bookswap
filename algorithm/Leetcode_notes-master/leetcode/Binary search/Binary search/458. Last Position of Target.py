'''
用这个模版做 其实就是当mid 是我们target的时候 我们用某个指针 去指向target
然后根据题目 我们决定用左指针 还是右指针
不断缩小范围 
'''

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if not nums:
            return -1
        left, right = 0, len(nums) -1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1