'''
使用DP。设这个DP[i][j]数组为以i, j位置为右下角顶点的能够成的最大正方形的边长。
初始化 我们遍历第一行 如果 matrix 中遍历到的元素是1 的话 我们把1 赋给对应的dp坐标
然后我们遍历 matrix，从第二行第二个开始遍历，因为我们dp需要左 上 左上的dp值，才可以推导， 所以我们从第二行第二个开始遍历
首先 我们每次到新的一行 要把第一格 给初始化
然后从第二格开始遍历 如果当前格子的值是1的话，我们就 取 以上 下 左上 为定点能够成最大正方形的边上 的最小值 + 1 赋给dp 现在的坐标
 + 1 是因为 要包含自己本身的格子
 遍历完一行以后
 拿这一行最大值 跟我们之前得到的最大值 进行比较 并且更新
 最后return 

'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        edge = int(max(matrix[0]))
        for i in range(len(matrix[0])):
            dp[0][i] = int(matrix[0][i])
        for i in range(1,len(matrix)):
            dp[i][0] = int(matrix[i][0])
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            edge = max(edge, max(dp[i]))
        return edge * edge