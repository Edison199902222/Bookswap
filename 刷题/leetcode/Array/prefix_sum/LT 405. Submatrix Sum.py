class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])
        for top in range(m):
            col_sum = [0] * n
            for down in range(top, m):
                prefix_sum = 0
                dic = {0: -1}
                for col in range(n):
                    col_sum[col] += matrix[down][col]
                    prefix_sum += col_sum[col]
                    if prefix_sum in dic:
                        return [(top, dic[prefix_sum] + 1), (down, col)]
                    dic[prefix_sum] = col
        return None
'''
我们确定上界跟下界以后 
再确定 col 边界
这样可以确定一个 大矩形
我们以每个col 找到它的 累加和
然后 只需要再大矩形内 找到 一个col 的累加和 跟大矩形累加和 相等，就证明在大矩形内部 有一个小矩形的和是0的
其实就是 确定完上界跟下界之后，把二维降成一维 使得 跟 138 题的原理是一样的
dic 记录prefix sum 跟对应的 col
'''