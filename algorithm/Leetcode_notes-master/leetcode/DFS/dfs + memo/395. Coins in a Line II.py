class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False
        self.memo = {}
        first_value = self.dfs(values, 0)
        return first_value * 2 > sum(values)

    def dfs(self, values, i):
        if i in self.memo:
            return self.memo[i]
        if i >= len(values):
            return 0
        if i == len(values) - 1:
            return values[-1]
        result = max(min(self.dfs(values, i + 2), self.dfs(values, i + 3)) + values[i],
                     min(self.dfs(values, i + 3), self.dfs(values, i + 4)) + values[i] + values[i + 1])
        self.memo[i] = result
        return result
'''
由小到大 的 记忆化搜索
我们站在first player 的角度 去看待， 
当还有i 个硬币时，第一个player 可以获取的最大值
base case 如果i 大于 value 长度了， 那肯定获取不了值了，因为没有硬币了
如果 只剩下一个硬币的时候，我们可以拿走最后一个
对于 剩下第i 个硬币 第一个player 可以拿多少取决于 
如果 我拿走一个的话， 对手拿走一个 那么我下一个状态是i + 2的状态， 如果对手拿走两个 那么下一个状态就是i + 3 的状态
但是 我和对手都是很聪明的，所以 对手肯定会使我最小化， 所以我们在取min（i+2,i+3) 并且要加上我们拿走的硬币的值
同理， 对于我拿走两个硬币的情况
然后 取两个情况的最大值， 就是如果剩下 i 个硬币，我拿走的最大值
把它放进memo中
并且return到上一层
所以，当剩下0个硬币的时候，我获取的最大值得出来了
如果这个最大值超过硬币总和的一半， 就说明我肯定赢
'''