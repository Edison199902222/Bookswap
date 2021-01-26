
'''
规律就是 第一排跟最后一排交换位置 第二排跟倒数第二排交换位置
然后matrix 从i+1开始 交换位置
matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
意思是对角线交换位置 但只需要交换一半
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # 先按照对角线交换位置
        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 然后逆转
        for i in range(m):
            matrix[i].reverse()


