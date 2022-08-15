class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # 对每一行求前缀和
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col - 1]
        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        original = self.matrix[row][col]
        # 找到原来的格子等于多少
        if col != 0:
            original -= self.matrix[row][col - 1]
        # 看更新后的val 跟 原val 的差
        difference = original - val
        # 更新每一格前缀和，因为当前格子如果更改了，后面的会收到影响，前面的前缀和不收到影响
        for i in range(col, len(self.matrix[0])):
            self.matrix[row][i] -= difference

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = 0
        # 对每一行 先加上 col2的前缀和，然后减去col1 的前缀和
        for i in range(row1, row2 + 1):
            sums += self.matrix[i][col2]
            if col1 != 0:
                sums -= self.matrix[i][col1 - 1]
        return sums

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)