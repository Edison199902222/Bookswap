'''
不在while中寻找答案
如果遇到target 我们就把end指向这个数
然后最后判断
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,5],0))