
'''
这道题需要先判断 是不是需要交换两个元素
因为如果 后面再判断 需不需要交换两个元素的话 left 与 right 会发生变化

'''
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if A is None:
            return []
        left = 0
        right = len(A) - 1
        while left <= right:
            if A[left] % 2 == 1 and A[right] % 2 == 0:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            if A[left] % 2 == 0:
                left += 1
            if A[right] % 2 == 1:
                right -= 1

        return A