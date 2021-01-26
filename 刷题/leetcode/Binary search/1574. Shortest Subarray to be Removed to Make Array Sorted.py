class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # 二分
        # 从头扫 到 最后一个符合条件的index
        # 后面扫 到最后一个符合条件的index
        # 对于每个后面扫的j 找到左边符合条件第一个小于等于 index j的 i ，左右两边都是递增的序列，j - i 就是 最少要减去的array
        n = len(arr)
        left_max = 0
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                left_max = i
            else:
                break
        # 到数组最后一个，说明全部符合条件
        if left_max == n - 1:
            return 0
        right_max = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                right_max = i
            else:
                break
        result = min(n - left_max - 1, right_max)
        for j in range(right_max, n):
            index = self.binary_search(arr, 0, left_max, arr[j])
            result = min(result, j - index - 1)
        return result

    def binary_search(self, arr, start, end, value):
        # 找的是最后一个 小于等于value 的
        left = start
        right = end
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] > value:
                right = mid
            else:
                left = mid
        if arr[right] <= value:
            return right
        if arr[left] <= value:
            return left
        return - 1

    class Solution(object):
        def findLengthOfShortestSubarray(self, arr):
            """
            :type arr: List[int]
            :rtype: int
            """
            n = len(arr)
            left_max = 0
            for i in range(1, n):
                if arr[i] >= arr[i - 1]:
                    left_max = i
                else:
                    break
            # 到数组最后一个，说明全部符合条件
            if left_max == n - 1:
                return 0
            right_max = n - 1
            for i in range(n - 2, -1, -1):
                if arr[i] <= arr[i + 1]:
                    right_max = i
                else:
                    break
            result = min(n - left_max - 1, right_max)
            # 找到从前到后符合标准的最大index i
            # 找到从后到前符合标准的最大index j 后
            # 尝试 从前到后 符合标准的index i 范围内，检查 最大index j是否大于i， 如果大于 i 到 j 区间可以尝试作为去掉的array
            # 不大于的话，那么j 需要往后移动，来保持两个区间
            for i in range(left_max + 1):
                if arr[i] <= arr[right_max]:
                    result = min(result, right_max - i - 1)
                elif right_max < n - 1:
                    right_max += 1
                else:
                    break
            return result
