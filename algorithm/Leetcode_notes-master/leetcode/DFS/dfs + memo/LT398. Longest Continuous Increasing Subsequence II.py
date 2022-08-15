class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """

    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        if not matrix:
            return 0
        self.memo = {}
        result = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result, self.dfs(i, j, matrix))
        return result

    def dfs(self, i, j, matrix):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        result = 1
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = i + x
            new_y = j + y
            if len(matrix) > new_x >= 0 and len(matrix[0]) > new_y >= 0 and matrix[new_x][new_y] < matrix[i][j]:
                result = max(result, self.dfs(new_x, new_y, matrix) + 1)
        self.memo[(i, j)] = result
        return result
'''
比较模版的一道题
我们使用记忆化搜索
遍历matrix 把每一个点作为我们的 终点，意思是 上下左右搜索 找所有比起始点 小的点
然后 result储存的是以当前点作为结尾， 最大的 longgest continuous increasing subsequence 初始化设置为1 因为 我们至少有一个点的时候 是1
然后上下左右搜索， 如果 新的坐标 没有越界 并且 比我们当前值小 那么我们就去新的点继续搜索， 得到的结果用来更新result
最后 上下左右搜索完成， 得到了以当前点作为终点 longgest continuous increasing subsequence 的result
用这个result 放进 memo中， 表示 以这个点 作为终点得到的result最大值， 以后如果再有访问这个点的话，就可以跳过
返回result
'''