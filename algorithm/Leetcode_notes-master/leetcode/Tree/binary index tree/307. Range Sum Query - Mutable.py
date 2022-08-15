'''
利用树状数组
binary index tree 每个孩子的 parent 是 自己的index 加上 自己二进制位最低位的和  x += x & (-x) 这就是x的父亲节点
树状数组 维持了一个 每个 父亲节点 是自己所有孩子的和的一个数组
所以 如果需要 0 到 j index中 所有的和
只需要 从j+1（ 因为binary index tree 从1 开始 不是从 0） 出发 遍历树状数组 每次加上父亲节点的值 i -= i & (-i) 就可以得到总的和
'''


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.orginal = nums
        self.index_tree = [0] * (self.n + 1)
        for i in range(self.n):
            k = i + 1
            while k < self.n + 1:
                self.index_tree[k] += nums[i]
                k += k & (-k)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        diff = val - self.orginal[i]
        self.orginal[i] = val
        i += 1
        while i < self.n + 1:
            self.index_tree[i] += diff
            i += i & (-i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        j = j + 1
        res = 0
        while j:
            res += self.index_tree[j]
            j -= j & (-j)
        while i:
            res -= self.index_tree[i]
            i -= i & (-i)
        return res


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        original = self.nums[i]
        if i != 0:
            original -= self.nums[i - 1]
        difference = original - val
        for i in range(i, len(self.nums)):
            self.nums[i] -= difference

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)