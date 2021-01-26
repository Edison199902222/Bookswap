class UnionFind(object):
    def __init__(self):
        self.father = {}
        self.count = {}

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            # 老大加上小弟的数量
            self.count[father_a] += self.count[father_b]

    def find(self, child):
        # 如果发现 自己就是父节点，说明找到最上面的父节点了
        if self.father[child] == child:
            return child
        # 把自己的父节点设置成最上面的父节点
        # 路径压缩，不用全部往上找
        self.father[child] = self.find(self.father[child])
        return self.father[child]

    def query(self, a):
        return self.count[self.find(a)]


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uf = UnionFind()
        for num in nums:
            if num not in uf.father:
                uf.father[num] = num
                uf.count[num] = 1
            if num + 1 in uf.father:
                uf.union(num, num + 1)
            if num - 1 in uf.father:
                uf.union(num, num - 1)

        max_value = 0
        for num in nums:
            max_value = max(max_value, uf.query(num))
        print(uf.count)
        return max_value
