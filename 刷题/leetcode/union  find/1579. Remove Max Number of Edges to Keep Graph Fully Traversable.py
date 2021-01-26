class Union_Find:
    def __init__(self, n):
        self.father = {i: i for i in range(n)}
        self.count = n
        # 可以查看 某一个node 有几个联通
        self.rank = [1] * n

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.father[y] = x
        self.rank[x] += self.rank[y]
        self.count -= 1

    def find_union(self, x, y):
        father_x, father_y = self.find(x), self.find(y)
        if father_x != father_y:
            self.union(father_x, father_y)
            # 表示，如果本来不是联通 return true
            return True
        # 如果本来是联通的 return false
        return False


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Alice
        uf1 = Union_Find(n)
        # Bob
        uf2 = Union_Find(n)
        result = 0
        # 思路：先把type 3 的联通，然后 以alice 跟 bob 的edge 去删掉本来已经联通的点
        # 只把type 3 连到 alice  跟 bob 的角度上
        for tp, start, end in edges:
            if tp != 3:
                continue
            # 如果 现在的start 跟 end 两个node 本来就是联通的，意味着是多月的edge 可以选择删除
            if not uf1.find_union(start - 1, end - 1) or not uf2.find_union(start - 1, end - 1):
                result += 1
        # 检查 type1 跟 type2的，如果两个点本来就是联通的，那么可以删除当前edge， 如果不是联通的，才需要这条edge
        for tp, start, end in edges:
            if tp == 1 and not uf1.find_union(start - 1, end - 1):
                result += 1
            if tp == 2 and not uf2.find_union(start - 1, end - 1):
                result += 1
        # 最后还需要检查，alice 跟 bob 的视角 是不是整个图联通的
        return result if uf1.count == 1 and uf2.count == 1 else - 1