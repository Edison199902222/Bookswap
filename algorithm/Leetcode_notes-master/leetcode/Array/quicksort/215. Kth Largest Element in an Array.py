'''
是用quick sort
每次quicsort 把大于pivot放在左边 把小于piviot放在右边
然后返回piviot的index
如果发现piviot的index就是第k个大的数 那么我们就返回
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, start, n, k):  # quick select
        pos = self.partition(nums, start, n)
        if pos == k - 1:
            return nums[pos]
        elif pos >= k:
            return self.quickSelect(nums, start, pos - 1, k)
        return self.quickSelect(nums, pos + 1, n, k)

    def partition(self, nums, left, right):
        pivot = nums[right]  # pick the last one as pivot
        i = left
        for j in range(left, right):  # left to right -1
            if nums[j] > pivot:  # the larger elements are in left side
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right]  # swap the i and the last element
        print(nums)
        return i


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quick_sort(nums, 0, len(nums) - 1, k)

    def quick_sort(self, nums, start, end, k):
        left = start
        right = end - 1
        pivot = nums[end]
        while left <= right:
            # 直到找到 一个不合法的left， 也就是不大于等于 pivot 的
            while left <= right and nums[left] >= pivot:
                left += 1
            # 找到一个不合法的right
            while left <= right and nums[right] <= pivot:
                right -= 1
            # 不想等时 进行交换
            if left < right:
                self.swap(nums, left, right)
        # left 就是 pivot 的位置
        self.swap(nums, left, end)

        if left + 1 == k:
            return nums[left]
        elif left + 1 < k:
            return self.quick_sort(nums, left + 1, end, k)
        else:
            return self.quick_sort(nums, start, left - 1, k)

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest([10, 1, 8, 2, 6], 2))
