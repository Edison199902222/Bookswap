'''
用回溯法
'''

class Solution:
    def exist(self, board, word) -> bool:
        if not word or not board or not board[0]:return False
        m = len(board)
        n = len(board[0])
        visit = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(i,j,board,visit,word,0):
                    return True
        return False


    def dfs(self,i,j,board,visit,word,inx):
        if inx == len(word):return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[inx] or visit[i][j]==1: return False
        visit[i][j] = 1
        existed = self.dfs(i-1,j,board,visit,word,inx+1) or self.dfs(i+1,j,board,visit,word,inx+1) or self.dfs(i,j-1,board,visit,word,inx+1) or self.dfs(i,j+1,board,visit,word,inx+1)
        visit[i][j] = 0
        return existed
if __name__ == "__main__":
    solution = Solution()
    x = [["a"]]
    y = "ab"
    z = solution.exist(x,y)
    print(z)
