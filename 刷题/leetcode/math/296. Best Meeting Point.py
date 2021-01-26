class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = []
        col = []
        m = len(grid)
        n = len(grid[0])
        # 把所有等于1 的点，分row 跟col 加入列表
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        # 分成两个列表的原因是 把两个列表中的中点取到，这个点就是到各个 其他点之间最小的距离
        # 点的个数为偶数， 则我们要找的点是 最里面的任何一个pair
        # 点的个数为奇数， 我们要找的点是 中位数
        row.sort()
        col.sort()
        result = 0
        row_mid = row[len(row) // 2]
        col_mid = col[len(col) // 2]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += abs(row_mid - i) + abs(col_mid - j)
        return result
'''
把二维转成一维
技巧就是 把row col 分开求出来
然后sort后
中间的 哪个点 就是我们的最佳点
'''