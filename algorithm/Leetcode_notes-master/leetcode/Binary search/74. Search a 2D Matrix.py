class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = (row * col) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            x = mid // col
            y = mid % col
            if matrix[x][y] >= target:
                right = mid
            elif matrix[x][y] < target:
                left = mid
        x = right // col
        y = right % col
        if matrix[x][y] == target:
            return True
        x = left // col
        y = left % col
        if matrix[x][y] == target:
            return True
        return False
'''
这是一个转化的二分法问题
因为矩阵的分布是从小到大的
所以 我们可以把整个矩阵编号
对每个数字，根据其下标i，j进行编号，每个数字可被编号为0～n*n-1
相当于是在一个数组中的下标。然后直接像在数组中二分一样来做。取的mid要还原成二位数组中的下标，i = mid/n, j = mid%n
'''
if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix([[1]],0))