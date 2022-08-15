
class UnionFind(object):
    def __init__(self, n):
        # 把所有的node 都创建一个circle， 以自己为父节点
        self.father = {i : i for i in range(n)}
        self.count = n
    # 设置交集
    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            self.count -= 1


    def find(self, child):
        # 如果发现 自己就是父节点，说明找到最上面的父节点了
        if self.father[child] == child:
            return child
        # 把自己的父节点设置成最上面的父节点
        # 路径压缩，不用全部往上找
        self.father[child] = self.find(self.father[child])
        return self.father[child]



class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count


'''
先遍历每一个朋友
用dfs搜索 对于每个朋友的朋友关系
如果朋友关系等于1 并且没有访问过的话 那么我们把关系 设置为true 继续以下一个朋友作为起点 继续进行dfs
'''
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.visit = [False]*len(M)
        circle = 0
        for i in range(len(M)):
            if not self.visit[i]:
                self.dfs(M, i)
                circle += 1
        return circle
    def dfs(self, M, i):
        for j in range(len(M)):
            if M[i][j] == 1 and not self.visit[j]:
                self.visit[j] = True
                self.dfs(M, j)