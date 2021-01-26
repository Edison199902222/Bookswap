class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                for j in range(i, n, i):
                    if s[0:i] != s[j:j + i]:
                        break
                    if j == n - i:
                        return True
        return False
'''
题目意思是 一个字符串是不是由其中的子字符串 重复组合的
所以 如果是的话 最大的子字符串应该是整个字符串长度的一半
所以 我们从1 遍历到一半的长度
而且 我们要检查 遍历长度时  n 是否 可以被 长度i 除尽
如果有余数 说明 组合不了
如果可以的话 那么我们继续 第二层遍历
遍历从i 到 长度n
每次往后检查 i 个长度 是不是跟前面的子串是不是一样的
如果不是 直接break
如果是就继续第二层遍历
直到遍历到 字符串的尾部
return true
'''