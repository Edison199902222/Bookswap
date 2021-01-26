class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1]+result[i-1][j])
            result.append(temp)
        return result[rowIndex]


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        self.memo = {}
        result = [0] * (rowIndex + 1)
        result[0] = result[-1] = 1
        for i in range(1, len(result) - 1):
            result[i] = self.dfs(rowIndex, i)
        return result

    def dfs(self, row, col):
        if col == 0 or row == col:
            return 1
        if (row, col) in self.memo:
            return self.memo[(row, col)]
        result = self.dfs(row - 1, col - 1) + self.dfs(row - 1, col)
        self.memo[(row, col)] = result
        return result

