
'''
建立 三维dp
dp[i][j][k]代表前i个物品 拥有j 个0空间 跟 k个 1 空间时 的时候 最多可以带几个物品
遍历物品， 先对于每个物品数有几个0 有几个 1
然后 如果当前空间不足以拿起当前物品时，  dp[s + 1][i][j] = dp[s][i][j] 意思时 前i 个物品时的最多可以带几个物品是跟 前i - 1个物品一样的数量， 因为没有选择当前的物品
如果 空间足够， 选择了当前物品时，我们可以 在 前i 个物品时的最多可以带几个物品是
跟 前i - 1个物品一样的数量 跟 前i个物品 体积 减去我们选择当前物品的体积 的最多可以带几个物品 取一个最大值 因为我们选择了当前物品
'''


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[[0 for i in range(n + 1)] for i in range(m + 1)] for i in range(len(strs) + 1)]
        for s in range(len(strs)):
            zeros = strs[s].count("0")
            ones = strs[s].count("1")
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[s + 1][i][j] = dp[s][i][j]
                    if i >= zeros and j >= ones:
                        dp[s + 1][i][j] = max(dp[s + 1][i][j],dp[s][i - zeros][j - ones] + 1)
        return dp[len(strs)][m][n]
'''
优化版本 
01 背包 内层循环 从大往小遍历
'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n + 1)] for i in range(m + 1)]
        for i in range(len(strs)):
            ones = strs[i].count("1")
            zero = strs[i].count("0")
            for j in range(m, zero - 1, -1):
                for k in range(n, ones - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zero][k - ones] + 1)
        return dp[m][n]
'''
空间上可以用滚动数组优化
并且 我们需要体积从后往前遍历，因为如果从前往后遍历，此时 如果更新后面需要前 i- 1 个物品的体积时，我们会找不到
因为前面的已经被更新成 前i 个物品的体积了
'''






class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp =[[0 for i in range(n + 1)] for i in range(m + 1)]
        for s in range(len(strs)):
            zeros = strs[s].count("0")
            ones = strs[s].count("1")
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    dp[i][j] = dp[i][j]
                    if i >= zeros and j >= ones:
                        dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]
