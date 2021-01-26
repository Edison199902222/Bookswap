'''
遍历matrix
先交换位置
然后再 0变1  1 变0
'''
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            left = 0
            right = len(A[i]) - 1
            while left < right:
                A[i][left],A[i][right] = A[i][right],A[i][left]
                left += 1
                right -= 1
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                elif A[i][j] == 1:
                    A[i][j] = 0
        return A