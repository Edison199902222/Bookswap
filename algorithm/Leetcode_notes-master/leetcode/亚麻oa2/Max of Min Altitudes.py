
def maxOfMinElevation(row, col, mat):
    dp = [[float("inf")] * (col) for i in range(row)]
    dp[0][0] = mat[0][0]
    for i in range(1, row):
        dp[i][0] = min(dp[i - 1][0], mat[i][0])
    for i in range(1, col):
        dp[0][i] = min(dp[0][i - 1], mat[0][i])

    for i in range(1, row ):
        for j in range(1, col):
            dp[i][j] = max(min(dp[i - 1][j], mat[i][j]), min(dp[i][j - 1], mat[i][j]))
    return dp[row - 1][col - 1]
def main():
    row = 2
    col = 2
    mat = [[5,1], [4,5]]
    temp = maxOfMinElevation(row, col, mat)
    print(temp)
main()