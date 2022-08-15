class Union_Find():
    def __init__(self):
        self.father = {}
        self.count = collections.defaultdict(int)

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            self.count[father_a] += self.count[father_b]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = Union_Find()
        result = -1
        for i in range(len(arr)):
            uf.father[arr[i]] = arr[i]
            uf.count[arr[i]] = 1
            # 每次检查这一轮要改变的count，如果 count 一直没有改变，那么我们可以在最后一轮检查就行了
            if arr[i] - 1 in uf.father:
                # 每次union 前 检查一次，看看 arr[i] - 1是不是符合条件的， 因为union过后，arr[i] - 1的count 会发生改变
                if uf.count[uf.find(arr[i] - 1)] == m:
                    result = i
                uf.union(arr[i], arr[i] - 1)
            if arr[i] + 1 in uf.father:
                # union 前检查一次，看看 arr[i] - 1 是不是符合条件， 因为union过后，arr[i] + 1的count 会发生改变
                if uf.count[uf.find(arr[i] + 1)] == m:
                    result = i
                uf.union(arr[i], arr[i] + 1)
        n = len(arr)
        # 最后检查，看最后一轮，有没有符合要求的
        for i in range(n):
            if uf.count[uf.find(i + 1)] == m:
                return n
        return result


class UnionFind(object):
    def __init__(self):
        self.father = {}
        self.count = {}
        self.count2 = collections.defaultdict(int)

    def union(self, a, b):
        father_a = self.find(a)
        father_b = self.find(b)
        if father_a != father_b:
            self.father[father_b] = father_a
            self.count2[self.count[father_a]] -= 1
            self.count2[self.count[father_b]] -= 1
            self.count[father_a] += self.count[father_b]
            self.count[father_b] = 0
            self.count2[self.count[father_a]] += 1

    def find(self, child):
        if self.father[child] == child:
            return child
        self.father[child] = self.find(self.father[child])
        return self.father[child]


class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        uf = UnionFind()
        result = -1
        for i in range(len(arr)):
            uf.father[arr[i]] = arr[i]
            uf.count[arr[i]] = 1
            uf.count2[1] += 1
            if arr[i] - 1 in uf.father:
                uf.union(arr[i], arr[i] - 1)
            if arr[i] + 1 in uf.father:
                uf.union(arr[i], arr[i] + 1)
            if uf.count2[m] > 0:
                result = i + 1
        return result


class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        # 记录每一个index 对应的 长度
        length = collections.defaultdict(int)
        # 记录在当前操作中有的长度
        count = collections.defaultdict(int)
        result = -1
        for i in range(len(arr)):
            # 找到当前要更新的value
            value = arr[i]
            # 看看value前面的长度，跟 value后面的长度
            left, right = length[value - 1], length[value + 1]
            # 当前长度就等于 左边长度 加上右边长度 加1
            current_length = left + right + 1
            # 更新 当前value 对应的长度
            length[value] = current_length
            # 对左边的也需要更新， left 到right 中间这些，不会再被call 了，所以不会被更新
            length[value - left] = current_length
            # 对右边也需要更新，
            length[value + right] = current_length
            # 因为左右结合了，所以left的长度贡献了
            count[left] -= 1
            # 左右结合了，right 的长度也贡献了
            count[right] -= 1
            # 更新当前长度
            count[current_length] += 1
            if count[m] > 0:
                result = i + 1
        return result
