class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        # write your code here
        self.memo = {}
        result = self.dfs(0, len(values) - 1, values)
        return result * 2 > sum(values)

    def dfs(self, left, right, values):
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        if left == right:
            return values[left]
        if left + 1 == right:
            return max(values[left], values[right])
        if left > right:
            return 0
        result = max(min(self.dfs(left + 1, right - 1, values), self.dfs(left + 2, right, values)) + values[left],
                     min(self.dfs(left + 1, right - 1, values), self.dfs(left, right - 2, values)) + values[right])
        self.memo[(left, right)] = result
        return result
'''
因为 这道题可以从头拿 也可以从尾部拿 所以只用dp[i】满足不了所有情况
所以 我们用i j 来代表 当前 剩下第i 到 j 个硬币时， 先手的最大值
然后就 dfs 
如果 i == j 说明 我们只剩下 一枚硬币了， 那么直接拿走 这一枚硬币
如果 left + 1 == right 代表 我们剩下两枚硬币， 先手肯定选这两个的最大值
越界 return 0
然后 我们就可以 有一个result 代表 当前 i j 情况下 先手的最大值 是依赖于两种大情况
第一种 如果我拿最左边的硬币 也就是第i 个的话， 那么对手有可能拿第j 个硬币 也有可能拿走 i + 1个硬币 
对手肯定想让我的值最小化，所以会让我在下一次情况的值是最小 所以我们用 min函数
同样的道理 第二种 如果我拿右边的硬币
对手也可能拿最左的 也可能等我拿走右边的 再拿右边的 我们也需要取 值最小的情况 加上我们现在拿走的右边的硬币 的值
最后 两个情况 取一个最大值 就是我们当前 i j 情况下能拿的最大值
然后放进memo 记录下来
return
时间复杂度 n^2
'''