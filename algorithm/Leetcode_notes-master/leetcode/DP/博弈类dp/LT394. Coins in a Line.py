'''
创建memo 记录 在每一次先手情况下剩下的coin 的个数 作为key 对应的是 true 或者 false
我们用dfs 来判断
base case 首先 如果 剩下小于 或者 等于0 个coin， 这时候 我们肯定输了
如果剩下 一个 或者两个， 这时候 我们肯定赢了 因为一次可以带走一个或者两个

其他情况 我们 用result 去记录， 此时 我们分成两种大情况， 一种是我们拿走一个 另一种是我们拿走两个的情况
拿走一个的情况又会分为 对手拿一个 或者拿两个
拿走两个情况又分成 对手拿一个 或者拿两个
这两种情况， 如果一个为true  就说明， 剩下n个时， 可以赢
如果都是false 说明 剩下n个时， 不可以赢
'''

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        self.memo = {}
        return self.dfs(n)
    def dfs(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 0:
            return False
        if n == 1 or n == 2:
            return True
        result = (self.dfs(n - 2) and self.dfs(n - 3)) or (self.dfs(n - 4) and self.dfs(n - 3))
        self.memo[n] = result
        return result

'''
也可以使用 dp 来解决
dp 来解决 是从小问题到 大问题 bottom to up 的一个过程
dp[i] 代表 当前剩下i个硬币，现在当前的人 取硬币以后的输赢
那么 转化方程 我们就需要 当前的人 可以取一个， 或者两个， 所以 依赖于 i - 1 跟 i - 2的状态
但是 取完硬币以后，就给对手取了， 所以 i - 1的状态 跟 i - 2 的状态 其实是对手的输赢情况
所以 我们需要取反， i - 1 或者 i -2 如果return的是true 代表 对手会赢，这代表我们是false
如果是false 代表对手会输， 代表我们是true
'''
class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        dp = [False] *3
        dp[1] = True
        dp[2] = True
        for i in range(3, n + 1):
            dp[i % 3] = not dp[(i - 1) % 3] or not dp[(i - 2) % 3]
        return dp[n % 3]