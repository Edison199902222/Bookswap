'''
1.从后往前，找到第一个 A[i-1] < A[i]的。也就是第一个排列中的  6那个位置，可以看到A[i]到A[n-1]这些都是单调递减序列。
        2.从 A[n-1]到A[i]中找到一个比A[i-1]大的值（也就是说在A[n-1]到A[i]的值中找到比A[i-1]大的集合中的最小的一个值）
        3.交换 这两个值，并且把A[n-1]到A[i]排序，从小到大。

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 如果从右往左，是升序列，没办法，这时候已经是最大了
        # 从右往左找到第一个降序的
        index = len(nums) - 2
        while index > - 1:
            if nums[index] < nums[index + 1]:
                j = pivot = index + 1
                # 寻找最接近 index 的数
                while j < len(nums) and nums[index] < nums[j]:
                    # 往右边找，找到极限以后，我们知道 从index 到 pivot 这个距离 是递减的
                    # 因为从右边遍历到左边，只有递减的顺序 我们才能移动到index，如果是递增的顺序的话，在之前就会被交换
                    pivot = j
                    j += 1
                nums[pivot], nums[index] = nums[index], nums[pivot]
                break
            index -= 1
        # 从index + 1 到结尾 升序排列
        nums[index + 1:] = nums[index + 1:][::-1]
