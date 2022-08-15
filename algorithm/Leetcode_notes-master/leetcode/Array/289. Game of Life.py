'''
// mark die -> live: -1
    // mark live -> die: 2

思路就是 先遍历 把每个位置的领据活着的数量算出来
然后 如果这个位置 是活着的话 那么邻居活着的数量超过三个 或者小于两个就要死 计为2
如果这个位置是死了 那么如果活着的邻居等于3的话 那就是活了
最后再update全局
'''

class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:return
        m = len(board)
        n = len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    live = self.count(board,i,j,m,n)
                    if live > 3 or live < 2:
                        board[i][j] = 2
                if board[i][j] == 0:
                    live = self.count(board, i, j,m,n)
                    if live == 3:
                        board[i][j] = -1
        self.update(board)
    def update(self,board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0
    def count(self,board, i, j, m, n):
        res = 0
        for newrow in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
            for newcol in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                if newrow >= 0 and newrow < len(board) and newcol>=0 and newcol<len(board[0]) and (board[newrow][newcol]==1 or board[newrow][newcol] == 2):
                    res+=1
        if board[i][j] == 1 or board[i][j] == 2:
            res -= 1
        return res
if __name__ == "__main__":
    solution = Solution()
    print(solution.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        00 -- 当前为死细胞且下一状态仍为死细胞
        01 -- 当前为活细胞且下一状态为死细胞
        10 -- 当前为死细胞且下一状态为活细胞
        11 -- 当前为活细胞且下一状态仍为活细胞
        对于前两种情况我们不需要做改动，因为给出的board内所有元素的倒数第二位均为0，所以需要修改的为后两种情况
        当死细胞周围正好有 3 个活细胞时，则满足第三种状态，所以需要重新赋值：board[i][j] = 2
        当活细胞周围正好有 2 个或者 3 个活细胞时，则满足第四种状态，所以需要重新赋值：board[i][j] = 3
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.caculate(m, n, i, j, board)
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3
                elif board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        return board

    def caculate(self, m, n, i, j, board):
        live = 0
        # 计算九个格子
        for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
            for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                # 计算， 使用 &，如果当前位是1 或者 3，那么 & 1 以后，还是1，如果 当前值是0 或者2 的话， & 1 后为0
                # 相当于 如果遇到 活细胞我们就加1， 遇到 死细胞 则 -1
                live += board[x][y] & 1
        # 减去自己的值
        live -= board[i][j] & 1
        return live


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        init state 0 = dead 1 = live
        00 means dead -> dead
        01 means live - > dead 少于两个活细胞， 多于 3个活细胞
        10 means dead - > live  有三个活细胞
        11 means live - > live 活细胞要等于2 个或者3 个
        '''
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                lives = self.caculate(i, j, m, n, board)
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 2
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

    def caculate(self, i, j, m, n, board):
        lives = 0
        for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
            for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                if board[x][y] == 1 or board[x][y] == 2:
                    lives += 1
        if board[i][j] == (1 or 2):
            lives -= 1
        return lives
