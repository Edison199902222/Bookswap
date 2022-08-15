class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 除数不能为0
        left = 1
        right = max(nums)
        nums.sort()
        while left + 1 < right:
            mid = (left + right) // 2
            if self.valid(nums, mid, threshold):
                right = mid
            else:
                left = mid
        if self.valid(nums, left, threshold):
            return left
        return right

    def valid(self, nums, mid, target):
        count = 0
        for num in nums:
            if num % mid != 0:
                count += (num // mid) + 1
            else:
                count += (num // mid)
        return count <= target