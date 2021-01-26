'''
建立dp
每个长度的最长cut 就是自己的长度-1 因为最坏情况就是 abcdefg 七个字母 都不是回文结构 那么要切6刀
然后从1 开始遍历到len+1
如果j 到 i 是 回文结构的话
那么dp i 就会等于 dp j 的+1
比如 abb
i = 3 的话 此时 j 如果等于1的话
j:i = bb
首先判断 bb是回文 是回文的话 那么 dp【3】 = dp【1】+1 因为分割成 a bb
只需要回文的bb切一刀 然后再加上 a的最小cuts 就可以 每个部分都是回文
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        for i in range(1,len(s)+1):
            if s[i:] == s[i:][::-1] and s[:i] == s[:i][::-1]:
                return 1
        dp = [ i-1 for i in range(len(s)+1)]
        for i in range(1,len(s)+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[-1]



'''
用 lc 5 的方法来判断中间的是不是回文
dp[i]代表 前i个字符串 最少需要切几刀可以使得前i个字符串变成回文
所以， 我们从头遍历字符串，枚举 i j（i <= j）
如果发现 第i 个字符 跟 j 个字符相等的话 摒弃i + 1 到j - 1 也是回文的话 
那么就说明i 到j 是回文字符串， 那么只需要 第 i个字符 之前的全部字符 是回文，就行了
所以推出了公式  dp[j] = min(dp[j], dp[i - 1] + 1)

'''


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [ i-1 for i in range(len(s) + 1)]
        p = [[False for x in range(n + 1)] for x in range(n + 1)]
        #the worst case is cutting by each char
        for j in range(1,len(s) + 1):
            for i in range(1, j + 1):
                if (s[i - 1] == s[j - 1] and (j - i < 2 or p[i + 1][j - 1])):
                    p[i][j] = True
                    dp[j] = min(dp[j], dp[i - 1] + 1)
        return dp[n]