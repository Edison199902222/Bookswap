import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        result = float("-inf")
        for left in range(col):
            sums = [0 for i in range(row)]
            for right in range(left, col):
                for row_number in range(row):
                    sums[row_number] += matrix[row_number][right]  # 保存从左边界到右边界， 每一个row 的和
                cur_max = float("-inf")  # 保存当前左右边界确定时， 上下边界确定时的最大值
                cur_sum = 0  # 当前大矩阵的sum
                cur_min_sum = [0]  # 所有小矩阵的sum
                for row_number in range(row):
                    cur_sum += sums[row_number]
                    pos = bisect.bisect_left(cur_min_sum, cur_sum - k)  # 二分查找， 查找在有序列表 a 中插入 x 的index, 如果x已经存在，则在左边插入
                    # 找到第一个大于等于curSum-k的值，那么curSum减去之前小矩形内元素和可以得到小矩形区域，且其元素和不超过k
                    if pos != len(cur_min_sum):  # 意思是如果pos 大于数组的长度的话，说明cur_sum - k 要大于 数组中所有的数字， 说明数组中不存在这样的数
                        cur_max = max(cur_max, cur_sum - cur_min_sum[pos])  # 如果找到的话， 那么我们就用大矩阵 减去找到的小矩阵的值，更新cur max
                    bisect.insort_left(cur_min_sum, cur_sum)  # 把当前大矩阵放进所有小矩阵中，因为我们的row 要增加了，曾经的大矩阵只能变成小矩阵了
                result = max(result, cur_max)
        return result


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        result = float("-inf")
        for row_number in matrix:
            for i in range(col - 1):
                row_number[i + 1] += row_number[i]  # 把row 的每一个number 都变成是前一个的累计和

        for left in range(col):
            for right in range(left, col):
                cur_max = float("-inf")
                cur_sum = 0  # 当前大矩阵
                cur_min_sum = [0]  # 所有小矩阵的sum
                for row_number in range(row):
                    # 统计当前大矩阵的累计和
                    if left > 0:  # 如果左边界大于0 的话， 那么我们大矩阵累计和 要减去前面一根的累计和
                        cur_sum += matrix[row_number][right] - matrix[row_number][left - 1]
                    else:  # 左边界不大于0， 直接加起来边界那一个col 的值， 因为右边界col的是每一行从index 0 到右边界的累加和
                        cur_sum += matrix[row_number][right]
                    pos = bisect.bisect_left(cur_min_sum, cur_sum - k)
                    if pos != len(cur_min_sum):
                        cur_max = max(cur_max, cur_sum - cur_min_sum[pos])
                    bisect.insort_left(cur_min_sum, cur_sum)  # 把当前大矩阵放进所有小矩阵中，因为我们的row 要增加了，曾经的大矩阵只能变成小矩阵了
                result = max(result, cur_max)
        return result


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        result = float("-inf")
        for left in range(n):
            for right in range(left, n):
                cur_submatrix = [0]
                cur_sum = 0
                for bottom in range(m):
                    # 算出大矩阵面积
                    if left == 0:
                        cur_sum += matrix[bottom][right]
                    else:
                        cur_sum += matrix[bottom][right] - matrix[bottom][left - 1]
                    # 找到当前大矩阵比 目标矩阵 大多少
                    # 尽量找到一个大于等于x 的， 目标就会小于等于 k
                    # x = cur - k， cur - x = k
                    x = cur_sum - k
                    pos = bisect.bisect_left(cur_submatrix, x)
                    # 说明里面有比x 大于等于的小矩阵
                    if pos < len(cur_submatrix):
                        result = max(result, cur_sum - cur_submatrix[pos])
                    bisect.insort_left(cur_submatrix, cur_sum)
        return result

