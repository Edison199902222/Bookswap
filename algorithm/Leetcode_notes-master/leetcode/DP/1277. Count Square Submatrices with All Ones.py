class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[0 for i in range(len(matrix[0]) + 1)]for i in range(len(matrix) + 1)]
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    count += dp[i][j]
        return count
'''
dp[i][j]表示以 i j 作为右下角定点时， 最多可以组成几个为1 的square sub matrix
跟221 同类题
'''