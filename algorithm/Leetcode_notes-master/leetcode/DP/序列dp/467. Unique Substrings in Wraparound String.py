class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = {x : 1 for x in p}
        length = 1
        for i in range(1,len(p)):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                length += 1
            else:
                length = 1
            dp[p[i]] = max(dp[p[i]], length)
        return sum(dp.values())

'''
dp[i]表示 以当前字符 i 结尾的 能够成的所有子字符串个数
初始化， 所有字符都可以组成1 个
然后 我们发现， 只要 当前字符 跟前一个字符在 字母表顺序是相邻的，那么我们就可以组成一个新的字符
并且 如果跟前一个字符跟前前一个字符 是相连的话，也可以组成新的字符
所以我们的length 是递增的，如果发现字母顺序是相邻的。一旦发现不相邻，初始化为1
'''