class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = len(nums1) + len(nums2)
        if k % 2 == 1:
            return self.helper(nums1, nums2, 0, 0, k // 2 + 1)

        return (self.helper(nums1, nums2, 0, 0, k // 2) + self.helper(nums1, nums2, 0, 0, k // 2 + 1)) / 2

    def helper(self, nums1, nums2, index1, index2, k):
        # 如果nums1里面的东西都被排除完了,说明答案不在nums1 中
        if index1 == len(nums1):
            return nums2[index2 + k - 1]
        # nums2 里面的东西被排除完了，说明答案不在nums2 中
        if index2 == len(nums2):
            return nums1[index1 + k - 1]
        if k == 1:
            return min(nums1[index1], nums2[index2])
        # 每次分一半，各自在nums1， num2 找答案
        gap = k // 2
        # 如果数组的所有数 都没有gap 多，不能移动B数组的index，因为不确定里面的大小，只能移动A数组的index，让gap缩小
        # 也因为 如果B数组中没有gap个的话， 那么可以确定 A数组中的含有 前k个元素 的数量 一定大于gap
        # 比如 我们要找第6 大的， gap 等于 3， a 数组有六个数， b数组有两个，那么a数组中我们知道 前六个中至少有四个
        # 所以删掉a 数组中的前三个 是很安全的
        if index1 + gap - 1 >= len(nums1):
            return self.helper(nums1, nums2, index1, index2 + gap, k - gap)
        if index2 + gap - 1 >= len(nums2):
            return self.helper(nums1, nums2, index1 + gap, index2, k - gap)
        if nums1[index1 + gap - 1] >= nums2[index2 + gap - 1]:
            return self.helper(nums1, nums2, index1, index2 + gap, k - gap)
        return self.helper(nums1, nums2, index1 + gap, index2, k - gap)

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1,2],[3,4]))