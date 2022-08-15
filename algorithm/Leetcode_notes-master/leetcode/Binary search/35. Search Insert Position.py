class Solution(object):
    def searchInsert(self, nums, target):
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
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return len(nums)
if __name__ =="__main__":
    soluiton = Solution()
    print(soluiton.searchInsert([1,3], 2))


