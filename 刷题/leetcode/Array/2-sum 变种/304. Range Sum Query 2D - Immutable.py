class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.matrix = matrix
        m = len(self.matrix)
        n = len(self.matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        count = 0
        if col1 == 0:
            while row1 <= row2:
                count += self.matrix[row1][col2]
                row1 += 1
        else:
            while row1 <= row2:
                count += self.matrix[row1][col2] - self.matrix[row1][col1 - 1]
                row1 += 1
        return count


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)