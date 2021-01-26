
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0: return None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i==0 or i == (len(board)-1) or j==0 or j==(len(board[i])-1):
                    if board[i][j] =="O":
                        self.dfs(i,j,board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] ="X"


    def dfs(self,i,j,board):
        if i < 0 or j < 0 or i>=len(board) or j>=len(board[i]):
            return None
        if board[i][j] == "X":
            return None
        if board[i][j] == "#":
            return None
        board[i][j] = "#"
        self.dfs(i+1,j,board)
        self.dfs(i-1, j, board)
        self.dfs(i,j+1, board)
        self.dfs(i,j-1, board)
if __name__ == "__main__":
    solution = Solution()
    list1 = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
    solution.solve(list1)
    print(list1)
