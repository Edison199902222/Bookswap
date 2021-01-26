class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * len(B[0]) for i in range(len(A))]
        # matrix[i][j] = A[i][k] * B[k][j]  k 是 A矩阵的col数量 或者是 B矩阵的row 数量
        # 传统数学方式算，横乘竖
        # 这种方式是，先算a 矩阵 的第一个 跟 b矩阵第一行所有都乘，然后乐嘉 a矩阵第二个 跟 b矩阵
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] == 0:
                    continue
                for j in range(len(B[0])):
                    if B[k][j] == 0:
                        continue
                    matrix[i][j] += A[i][k] * B[k][j]
                    print(matrix)
        return

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        matrix = [[0] * len(B[0]) for i in range(len(A))]
        # 通用算法
        # 固定住第行
        for i in range(len(A)):
            # 固定住第列
            for j in range(len(B[0])):
                # 对于a 来说，每次往右移动一个， 对于b来说 每次往下移动，达到横乘竖的目的
                for k in range(len(A[0])):
                    matrix[i][j] += A[i][k] * B[k][j]
        return matrix
