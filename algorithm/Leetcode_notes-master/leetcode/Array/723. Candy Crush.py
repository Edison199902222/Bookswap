class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(board)
        n = len(board[0])
        # 思路： 统计每一行，每一个col 有多少个需要被消掉，记录到set中
        # 遍历set， 消掉的设置为0
        # 从col 最后一位开始，利用双指针，交换位置
        while True:
            crush = set()
            # 看每一行有没有一样的， 不能是0
            for i in range(m):
                for j in range(n):
                    if j >= 2 and board[i][j] == board[i][j - 1] == board[i][j - 2] and board[i][j] != 0:
                        crush |= {(i, j), (i, j - 1), (i, j - 2)}
            # 看每一列有没有3 个连续的，并且不能是0
            for j in range(n):
                for i in range(m):
                    if i >= 2 and board[i][j] == board[i - 1][j] == board[i - 2][j] and board[i][j] != 0:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}
            if not crush:
                break
            else:
                for i, j in crush:
                    board[i][j] = 0
            self.drop(board)
        return board

    # drop same as 283
    def drop(self, board):
        m = len(board)
        n = len(board[0])
        # 从每一行的结尾开始，index 指向为0的区域，另一个指针指向不为0的区域
        # 另一个指针遇到不为0，就跟index 指向0的区域 交换位置，然后index - 1
        for j in range(n):
            index = m - 1
            for i in range(m - 1, -1, -1):
                if board[i][j]:
                    board[i][j], board[index][j] = board[index][j], board[i][j]
                    index -= 1


