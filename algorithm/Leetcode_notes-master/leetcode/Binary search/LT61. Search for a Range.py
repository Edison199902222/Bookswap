class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0:
            return [-1, -1]
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
        if A[left] == target:
            left_bound = left
        elif A[right] == target:
            left_bound = right
        else:
            return [-1,-1]
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid
        if A[right] == target:
            right_bound = right
        else:
            right_bound = left
        return [left_bound,right_bound]
'''
两次二分法
求出上下界
'''