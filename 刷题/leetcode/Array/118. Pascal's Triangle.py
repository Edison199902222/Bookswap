'''
创建 一个result
其实就是 每一行的第j个会等与上一行的j-1 + j 并且 每一行0 和 i 是1
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    haha = result[i-1][j-1]
                    hu = result[i - 1][j]
                    row.append(result[i-1][j-1] + result[i-1][j])
            result.append(row)
        return result
if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(3))


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        self.memo = {}
        for i in range(numRows):
            temp = [1]
            for j in range(i):
                temp.append(self.dfs(i, j + 1))
            result.append(temp)
        return result

    def dfs(self, row, col):
        if col <= 0 or col >= row:
            return 1
        if (row, col) in self.memo:
            return self.memo[(row, col)]
        result = self.dfs(row - 1, col - 1) + self.dfs(row - 1, col)
        self.memo[(row, col)] = result
        return result
