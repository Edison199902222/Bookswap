'''
作为皇后 每一行只能有一个 并且 不能跟同一行 或者 同一列 或者 斜着 反斜着 一起有皇后
那么 我们把 col row 还有 pie na作为四个set 记录 当前格子如果放了皇后 符不符合规则
每次 进行下一次递归时 row + 1
每次递归时 检查 这一行 每一个col 可不可以放皇后 如果放了皇后 那么我们就进行下一次递归 进入下一个row
最后 需要用 generate函数 形成board
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []
        self.row = set()
        self.col = set()
        self.pie = set()
        self.na = set()
        self.result = []
        self.dfs(n, 0, [])
        return self._generate(n)

    def dfs(self, n, row, path):
        if row >= n:
            self.result.append(path)
        for col in range(n):
            if col in self.col or row in self.row or row + col in self.pie or row - col in self.na:
                continue
            self.row.add(row)
            self.col.add(col)
            self.pie.add(col + row)
            self.na.add(row - col)
            self.dfs(n, row + 1, path + [col])
            self.row.remove(row)
            self.col.remove(col)
            self.pie.remove(col + row)
            self.na.remove(row - col)

    def _generate(self, n):
        board = []
        result = []
        for i in self.result:
            for j in i:
                board.append("." * j + "Q" + "." * (n - j - 1))
        for i in range(0, len(board), n):
            result.append(board[i:i + n])
        return result
if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))