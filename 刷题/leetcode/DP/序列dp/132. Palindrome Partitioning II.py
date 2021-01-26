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