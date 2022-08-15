class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0] * n
        self.col = [0] * n
        self.dia1 = 0
        self.dia2 = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            mark = 1
        else:
            mark = -1
        self.row[row] += mark
        self.col[col] += mark
        if row == col:
            self.dia1 += mark
        if row + col == self.n - 1:
            self.dia2 += mark
        if self.row[row] == self.n or self.col[col] == self.n or self.dia1 == self.n or self.dia2 == self.n:
            return 1
        if self.row[row] == -self.n or self.col[col] == -self.n or self.dia1 == -self.n or self.dia2 == -self.n:
            return 2
        return 0
'''
不用创建网格, 只需记录每个行、列和两条对角线的下棋的值。
对于每个下棋，对于玩家1的下棋赋值是1，对于玩家2的下棋赋值是-1。
然后我们只需要检查当前所在的行/ 列/ 对角线的下棋的值是否等于n或-n
'''


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0 for i in range(n)]
        self.col = [0 for i in range(n)]
        self.diagnal = 0
        self.reverse_diagnal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row == col:
                self.diagnal += 1
            if row + col == self.n - 1:
                self.reverse_diagnal += 1
            if self.n in self.row:
                return 1
            if self.n in self.col:
                return 1
            if self.diagnal == self.n:
                return 1
            if self.reverse_diagnal == self.n:
                return 1
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row == col:
                self.diagnal -= 1
            if row + col == self.n - 1:
                self.reverse_diagnal -= 1
            if -self.n in self.row:
                return 2
            if -self.n in self.col:
                return 2
            if self.diagnal == -self.n:
                return 2
            if self.reverse_diagnal == - self.n:
                return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)