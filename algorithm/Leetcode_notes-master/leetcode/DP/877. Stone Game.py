class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0 for i in range(len(piles))] for i in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for distance in range(1, len(piles)):
            for i in range(len(piles) - distance):
                j = i + distance
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return True if dp[0][len(piles) - 1] > 0 else False


'''
dp[i][j]的意思是 从i 到 j 这个区间 先手的人 比对手 多赢多少个子
所以 我们最后只要判断从dp 从0 到 n -1 这个区间 的数字是正的话 那么证明 alex 会赢
如果是负数 则会输
我们假设 两个人都会选择最优解
初始化dp 
长度为1 的区间中 i 到 i， 因为区间只有一个数字 所以肯定就比对手多赢这个数字 也就是piles i
然后我们从长度为2 一直扩大到长度为n
我们从 index 0 开始 
dp[i][j] 如果 alex 选择 数组第一个 也就是 i 的话 那么他会比 对手多赢 【 piles[i] - dp[i + 1][j] 】
dp[i + 1][j] 意思是 对手会从 i + 1 到j 这个区间 变成先手的人
如果alex 选择j 的话，也就是数组最后一个石头， 那么他会比 对手多赢 piles[j] - dp[i][j - 1]
dp[i][j - 1] 意思是 对手会变成 从i 到j -1 这个区间 变成先手的人
'''

'''
用dfs + memo 的写法
代表 石头如果留下 从i 到j 这么多石头的话，先手的人会有多少的石头
'''


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.memo = {}
        result = self.dfs(0, len(piles) - 1, piles)
        return result * 2 > sum(piles)

    def dfs(self, i, j, piles):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        if i > j:
            return 0
        if i == j:
            return piles[i]
        if i + 1 == j:
            return max(piles[i], piles[j])
        result = max(piles[i] + min(self.dfs(i + 2, j, piles), self.dfs(i + 1, j - 1, piles)),
                     piles[j] + min(self.dfs(i + 1, j - 1, piles), self.dfs(i, j - 2, piles)))
        self.memo[(i, j)] = result
        return result


'''
dp另一种思想
dp[i][j]代表如果留下 i 到 j的石头的话，先手可以获得的石头的数值是多少
得从bottem to top
所以， 我们从石头的尾部开始枚举
但是 j 的数量我们每次需要跳2， 因为每一次 对手也会选择一次石头
'''


class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        dp = [[0 for i in range(len(piles))] for i in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for i in range(len(piles) - 1, -1, -1):
            for j in range(i + 1, len(piles), 2):
                if i + 1 == j:
                    dp[i][j] = max(piles[i], piles[j])
                else:
                    dp[i][j] = max(piles[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                                   piles[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))
        return True if dp[0][len(piles) - 1] * 2 > sum(piles) else False
