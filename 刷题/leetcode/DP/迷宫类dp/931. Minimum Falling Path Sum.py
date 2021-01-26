class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0
        self.memo = {}
        m = len(A)
        n = len(A[0])
        result = float("inf")
        for j in range(n):
            result = min(result, self.dfs(0, j, A, m, n))
        return result

    def dfs(self, i, j, A, m, n):
        if i < 0 or j < 0 or i >= m or j >= n:
            return float("inf")
        if i == m - 1:
            return A[i][j]
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        result = min(self.dfs(i + 1, j, A, m, n), self.dfs(i + 1, j - 1, A, m, n), self.dfs(i + 1, j + 1, A, m, n)) + \
                 A[i][j]
        self.memo[(i, j)] = result
        return result
