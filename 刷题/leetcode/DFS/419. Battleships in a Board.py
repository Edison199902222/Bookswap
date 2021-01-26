class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        m = len(board)
        n = len(board[0])
        result = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X" and (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."):
                    result += 1
        return result
'''
找船头的位置
只要左边没有x 上面没有x 就是船头！
'''