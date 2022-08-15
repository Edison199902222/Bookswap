'''
先建立我们的结果 list
然后从后往前 我们找到整个list 最大值 一个一个放进去
这样就不用任何build in function
'''

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [None] * len(A)
        left = 0
        right = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[i] = A[left] ** 2
                left += 1
            else:
                result[i] = A[right] ** 2
                right -= 1
        return result
