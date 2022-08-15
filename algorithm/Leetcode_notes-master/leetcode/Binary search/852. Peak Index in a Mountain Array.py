class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] > A[mid - 1]:
                left = mid
            else:
                right = mid
        if A[left] > A[left + 1] and A[left] > A[left - 1]:
            return left
        else:
            return right
'''
二分法 
套模版
每次跟 mid 前一个比较
来决定 往哪个区间缩
'''