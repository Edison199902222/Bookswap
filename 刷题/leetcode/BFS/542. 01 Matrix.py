class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        deque = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    deque.append((i,j))
                else:
                    matrix[i][j] = 1000
        while deque:
            x, y = deque.popleft()
            for i,j in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_x = x + i
                new_y = y + j
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y] + 1:
                    matrix[new_x][new_y] = matrix[x][y] + 1
                    deque.append((new_x, new_y))
        return matrix
'''
做bfs 本来是算 1 到0 的位置 我们可以反过来想 把0 作为起始点 找所有1 的位置
我们遍历矩阵 把所有0 的位置 作为起点 加到queue中， 遇到 不是0 的位置， 我们设为1000， 随便设置一个最大值就行，表示还没有找到0
然后 我们遍历deque，
把每一个0 作为起始点pop出来
上下左右搜索， 如果 新的坐标合法的话 并且 新的坐标的值（到0 的距离） 是大于 我们当前坐标的值 + 1， 说明我们有必要更新它， 那么我们就可以更新新的坐标的值
并且把新坐标放进queue中
'''