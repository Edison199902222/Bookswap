'''
先把matrix 建立
然后加数
加完以后 遍历matrix 数
'''
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = [[0 for i in range(m)]for j in range(n)]
        count = 0
        for i,j in indices:
            for col in range(m):
                matrix[i][col] += 1
            for row in range(n):
                matrix[row][j] += 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] % 2 == 1:
                    count+=1
        return count
