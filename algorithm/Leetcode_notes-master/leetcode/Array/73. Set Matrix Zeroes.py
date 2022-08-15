class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # 用第一行， 跟 第一列来表示 这一行 这一列有没有
        first_row = False
        first_col = False
        # 第一列有0的话，设置true
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break
        # 第一行有0 的话 设置true
        for i in range(n):
            if matrix[0][i] == 0:
                first_row = True
                break
        # 用第一行，第一列 来判断 本行 或者本列有没有0
        # 如果遍历到0， 设置本行 以及本列的第一个元素为0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 遍历第一列，如果有0，此行全部设为0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        # 遍历第一行，如果有0， 此列全为0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        # 检查第一行，第一列是否有0
        if first_row:
            for i in range(n):
                matrix[0][i] = 0
        
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
        
                    