'''
dp
比较两个字符串一般都用dp
如果字符串当前相等 那么数量就会等于 去掉这个字符串之前的 + 跳过这个字符串的
dp[i][j] = dp[i-1][j-1] + dp[i][j-1] i表示t中的字符串 j表示s中的字符串
'''


class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)
        # dp[i][j]表示 s的前i个元素 有几种不同的子序列 fit t 的前 j 个元素
        dp = [[0] * (n + 1) for i in range(m + 1)]

        # s的前i个元素 有几种不同的子序列 fit t 的前0个元素
        # t = “ ”， s的前任何个元素都有1种方法，就是空串 当s = “”， t = “” 他们是匹配的
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 相等的话，可以由 i - 1 j -1 加上 i j 得到
                # 那么也可以我们不算上i， 看看 i - 1 到j 有几种
                # 所以有两部构成
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                # 如果s[i]!=t[j]的话，说明s[i]指望不上，我们就将注意力放在s[1:i-1]上，
                # 看里面有多少个不同子序列等于t[1:j]，直接拿过来用就行，反正加上了s[i]也不管事
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]
if __name__ == "__main__":
    solution = Solution()
    a = "rabbbit"
    b =  "rabbit"
    print(solution.numDistinct(a,b))