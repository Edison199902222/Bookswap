class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.memo = {}
        return self.dfs(0, len(A) -1, A)
    def dfs(self, i, j, A):
        if (i,j) in self.memo:
            return self.memo[(i,j)]
        if i == j or i == j - 1:
            return 0
        result = float("inf")
        for k in range(i + 1, j):
            result = min(result, A[i] * A[k] * A[j] + self.dfs(i, k, A) + self.dfs(k, j, A) )
        self.memo[(i,j)] = result
        return result
'''
这题就是跟312 一样的题 思路都是一样的
dp[i][j]表示 用i j 作为三角形的两个点，然后它的最小值是多少
我们只需要确定第三个点 就能知道一个三角形的值， 我们遍历 i + 1 到j， 枚举每一个点作为第三个点
然后dfs 求解
'''

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = [[float("inf") for i in range(len(A))]for i in range(len(A))]
        n = len(A)
        # 初始化 因为任何两个点确定不了三角形
        for i in range(len(A) - 1):
            dp[i][i + 1] = 0
        for gap in range(2, len(A)):   # 先枚举距离， 最小就是2， 因为小于2 就没有三个点，少于三个点无法构成三角形
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[k] * A[j])
        return dp[0][n - 1]