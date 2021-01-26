'''
dp
二维数组 i j 表示 s的i个 跟p的j个 是不是匹配的
先初始化数组
p中 如果字符串当前指向的是 * 那么取决于 p减去*跟之前那个字母
动态规划令 dp[i][j] 为string s 前i位是否匹配p的前j位，为bool类型，例如dp[1][1]为s[0]、p[0]是否匹配，初始化后剩下的判断分为以下几种情况分析：
p[j] == s[i] 或者 p[j] == '.' #匹配成功跟前面匹配一致
dp[i+1][j+1] = dp[i][j]
p[j] == '*' 这时又分两种情况
1。 s[i-1]!=p[j-2]
意思是 s的最后一个 跟p在*之前的那个不一样 说明 * 只能消除
dp[i][j] = dp[i][j-2]
2。  s[i - 1] == p[j - 1] or p[j - 1] == "."
s 与 p 的最后一个是一样的，
dp[i][j] = dp[i][j-2] or dp[i-1][j]  # 那么 * 可以算0 个 或者 多个之前的字符
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None or p is None:
            return False
        dp = [[False for i in range(len(p) + 1)] for x in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):  # 表示 如果p当前的是*的话 把*当作0 那么就会等于p 去掉两个字符的
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":  # 如果当前s p 的字符都相等 那么取决于两个之前的字符想不相等
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j-1] == "*":
                    if p[j-2] == "." or p[j-2] == s[i-1]:   # 如果当前字符是*的话，并且*之前的字符 与 s的最后一位相等
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]  # 那么 * 可以算0 个 或者 多个之前的字符，
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]
if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("aa","a"))


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True
        # 特殊情况，如果dp[0][i]，s是空的，怎么让p 匹配呢
        # 只有一种情况，就是即类似"a*b*c*"这类的，并且这里的星号都代表重复零次
        for i in range(2, n + 1):
            if p[i - 1] == "*" and dp[0][i - 2]:
                dp[0][i] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] and dp[i - 1][j - 1]:
                    dp[i][j] = True
                elif p[j - 1] == "." and dp[i - 1][j - 1]:
                    dp[i][j] = True
                elif p[j - 1] == "*":
                    # 重复 0 次
                    flag1 = dp[i][j - 2]
                    # 如果重复n次的话，那么s的最后一个要跟p的倒数第二个相等才行，不然重复多少次都不一样
                    # 第二种可以认为是重复了若干次。不管重复了几次，都要求s[i]必须是与p[j-1]相匹配的字母。这说明什么呢？刨除s[i]之外，前面的字符串也必须与p[1..j]匹配
                    # 为什么要看dp[i - 1][j]， 因为如果重复了n次的话，那么去掉s的最后一个也会是匹配的， 通过 把 * 看成0次
                    if (s[i - 1] == p[j - 2] or p[j - 2] == ".") and dp[i - 1][j]:
                        flag2 = True
                    else:
                        flag2 = False
                    dp[i][j] = flag1 or flag2
        return dp[m][n]