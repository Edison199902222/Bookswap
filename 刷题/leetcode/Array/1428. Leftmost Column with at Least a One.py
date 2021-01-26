# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        row_max, col_max = binaryMatrix.dimensions()
        col_max -= 1
        row = 0
        result = -1
        while col_max >= 0 and row < row_max:
            if binaryMatrix.get(row, col_max) == 1:
                result = col_max
                col_max -= 1
            else:
                row += 1
        return result
'''
从右上角 到左下角搜索
'''