'''
这是二分查找的一种变体，找到区间中点mid如果值比首个元素大（注意相等这种情况也要纳入），说明数组前半部分是升序的，后半部分右旋转，否则反之。
如果中间结点 mid 大于首个元素 那么 我们继续利用首个元素进行判断
如果这个节点大于我们的target 并且target比首个节点大的话 说明target 在左边
不然的话 说明target在右边
如果中间节点 小于首个元素的话 那么我们可以知道说明 我们这个节点处于被旋转之中并且 利用最后一个元素进行判断
 这时候 再判断 如果 target大于我们的mid 并且小于我们的右边节点的话
说明 处于我们的右边
反之 处于我们的左边
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                if nums[mid] >= target >= nums[left]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[right] >= target >= nums[mid]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 通过单调性来判断
        # 可以发现的是，我们将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的。
        # 拿示例来看，我们从 6 这个位置分开以后数组变成了 [4, 5, 6] 和 [7, 0, 1, 2] 两个部分，其中左边 [4, 5, 6] 这个部分的数组是有序的，其他也是如此。
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            # 如果mid 大于尾部元素，说明 mid 到 right 这一段 不具有单调性
            # 那么 左边 到 mid 这段，有可能是单调递增的， 所以接着判断
            # 如果target 小于left， 或者 大于mid， 说明答案不在 left  到 mid 这个区间
            if nums[mid] >= nums[right]:
                if nums[mid] >= target >= nums[left]:
                    right = mid
                else:
                    left = mid
            # 如果 mid 小于尾元素，说明mid 到 right 这一段有可能是单调递增的
            # 所以接着判断，target 是不是在 这个区间内，不是的话 就抛弃
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


if __name__ =="__main__":
    solution = Solution()
    print(solution.search([1,3,1,1,1],3))
