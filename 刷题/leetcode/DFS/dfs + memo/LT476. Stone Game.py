class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def stoneGame(self, A):
        # write your code here
        self.memo = {}
        return self.dfs(0, len(A) - 1, A)

    def dfs(self, left, right, A):
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        if left >= right:
            return 0
        sums = sum(A[left: right + 1])
        min_cost = float("inf")
        for mid in range(left, right):
            left_one = self.dfs(left, mid, A)
            right_one = self.dfs(mid + 1, right, A)
            min_cost = min(min_cost, left_one + right_one + sums)
        self.memo[(left, right)] = min_cost
        return min_cost
'''
left right 表示 现在有index left to right 的石子合并到一起所需要的最小cost
每次 我们先计算出 最后一次合并的时候 要多少的cost 也就是sum left right就能知道
然后我们枚举 mid， 每一次以mid 为分界点， 把 left right 分成 left 到 mid， mid + 1  到 right这两堆 石子
然后dfs 搜索  left 到 mid需要多少cost，mid + 1 到right 需要多少cost， 再加上之前算的sum，就是把left 到right 都合并到一起所需要的cost
然后更新min cost， mid + 1继续计算新的cost

最后 计算出最小的min cost了之后 
用它更新memo
并且return min cost
'''