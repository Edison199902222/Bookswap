'''
从第一行最右边开始搜索
如果这个数字比target 大 那么说明在左边
如果比target小 说明在下面
time :O(m + n)
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0:
            return  False
        m = len(matrix)
        n = len(matrix[0])
        cur_row = 0
        cur_col = n-1
        while cur_row < m and cur_col >= 0:
            if matrix[cur_row][cur_col] == target:
                return True
            elif matrix[cur_row][cur_col] > target:
                cur_col-=1
            elif matrix[cur_row][cur_col] < target:
                cur_row+=1
        return False