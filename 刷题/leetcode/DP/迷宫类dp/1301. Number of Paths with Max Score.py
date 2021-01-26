class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        self.memo = {}
        m = len(board)
        mod = 10 ** 9 + 7
        max_score, max_path = self.dfs(board, m - 1, m - 1, mod)
        return [max_score % mod, max_path % mod] if max_score > float("-inf") else [0, 0]

    def dfs(self, board, i, j, mod):
        if i == 0 and j == 0:
            return [0, 1]
        if board[i][j] == "X":
            return [float("-inf"), float("-inf")]

        if i < 0 or j < 0:
            return [float("-inf"), float("-inf")]

        if (i, j) in self.memo:
            return self.memo[(i, j)]

        score1, path1 = self.dfs(board, i - 1, j, mod)
        score2, path2 = self.dfs(board, i - 1, j - 1, mod)
        score3, path3 = self.dfs(board, i, j - 1, mod)

        max_score = max(score1, score2, score3)
        max_path = 0
        if score1 == max_score:
            max_path += path1
        if score2 == max_score:
            max_path += path2
        if score3 == max_score:
            max_path += path3
        if board[i][j] != "S":
            max_score += int(board[i][j])
        self.memo[(i, j)] = [max_score, max_path]
        return [max_score, max_path]

