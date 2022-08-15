class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def isvalid(board, row, col, val):
            for i in range(9):
                if board[i][col] == val: return False
            for i in range(9):
                if board[row][i] == val: return False
            x = row - row % 3
            y = col - col % 3
            for i in range(3):
                for j in range(3):
                    if board[i + x][y + j] == val:
                        return False
            return True

        def helper(board, row, col):
            if row == 9:
                return True
            if col >= 9:
                return helper(board, row + 1, 0)
            if board[row][col] != '.':
                return helper(board, row, col + 1)

            for i in range(1, 10):
                if isvalid(board, row, col, str(i)):
                    board[row][col] = str(i)
                    if helper(board, row, col + 1) == True:
                        return True
                    board[row][col] = '.'
            return False

        helper(board, 0, 0)


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.dfs(board, 0, 0)
        return board

    def dfs(self, board, row, col):
        if row == len(board):
            return True
        if col >= len(board[0]):
            return self.dfs(board, row + 1, 0)
        if board[row][col] != ".":
            return self.dfs(board, row, col + 1)
        # 对当前格子，选一个值
        for i in range(1, 10):
            if self.valid(board, row, col, str(i)):
                board[row][col] = str(i)
                if self.dfs(board, row, col + 1):
                    return True
                board[row][col] = "."
        return False

    def valid(self, board, row, col, val):
        # 检查submatrix 是否有重复
        for i in range(9):
            # 检查同一行有没有重复
            if board[row][i] == val:
                return False
            # 检查统一竖列有没有重复
            if board[i][col] == val:
                return False
            # row // 3 * 3 意思是找到所属的submatrix中，第一个格子的row的坐标 因为向下取整
            # + i // 3 意思是， 当前是第几个格子， 就加上对应的值，如果是第4个格子，那么就会变成 3 // 3 会加上1
            # 因为第四个格子的row 在第一个格子的下方
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == val:
                return False
        return True

