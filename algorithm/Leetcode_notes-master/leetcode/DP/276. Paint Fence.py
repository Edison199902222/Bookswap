class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k
        different = k * (k - 1)
        for i in range(3, n + 1):
            same,different = different, same * (k - 1) + different * (k - 1)
        return same + different

'''
采用动态规划的思想。
dp[i]=(k-1)×(dp[i-1]+dp[i-2])
dp[i-1]×(k-1)代表当前格子的颜色和前一个不同的方案
dp[i-2]×(k-1)代表当前格子的颜色和前一个相同的方案, 但我们必须和前前个栅栏是不相同的
'''
class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [0, k, k * k]
        if n <= 2:
            return dp[n]
        if n >= 3 and k == 1:
            return 0
        for i in range(2, n):
            dp.append(dp[-1] * (k - 1) + dp[-2] * (k - 1))
        return dp[-1]
'''
用 same 记录 每个柱子 跟之前一样刷法 状态
diff 记录表示 跟之前柱子不一样的刷法 状态
对于每个柱子
我们可以选择 跟 之前一个柱子一样的刷法 或者跟之前的柱子不一样的刷法
如果选择跟前面一个柱子一样的刷法的话， 那么我们需要 前面的柱子选择跟前前个柱子不一样刷法的状态 
所以 现在柱子如果选一样刷法 一共有 dff * 1， 1 表示我们需要跟之前一样的刷法 只能选一个刷法
如果选择不一样刷法的话 那么我们可以选择之前柱子 跟前前柱子一样的刷法 或者 跟前前柱子不一样刷法的状态
所以 是有两部分加起来， same * (k - 1) 表示 前一个选择了前前刷法一样 当前我们可以选择 除去跟前一个刷法一样的其他颜色 也就 k - 1
 different * (k - 1) 表示 前一个选择了跟前前刷法不一样 那么我们当前可以选择 除去跟前一个刷法一样的其他颜色 也就 k - 1
 最后return 两个刷法加起来就可以
'''
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if not n:
            return 0
        # 题目要求说，不允许有三个栅栏相同颜色
        # 所以对于当前栅栏来说，刷什么颜色 取决于 前面一个，跟前前一个
        # 要么不能跟前一个颜色相同，要么不能跟前前个相同
        dp = [0 for i in range(n + 1)]
        dp[1] = k
        dp[2] = k * k
        for i in range(3, n + 1):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.numWays(3,3))