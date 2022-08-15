'''
运用dfs去判断是否有效
rows cols 是九个set组成的list
sub——board 是三个set组成的list的list[[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]
'''


class Solution:
    def isValidSudoku(self, board):
        if len(board) != 9 and len(board[0]) != 9:
            return False

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_board = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    if any([board[i][j] in rows[i], board[i][j] in cols[j], board[i][j] in sub_board[i // 3][j // 3]]):
                        return False

                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sub_board[i // 3][j // 3].add(board[i][j])

        return True