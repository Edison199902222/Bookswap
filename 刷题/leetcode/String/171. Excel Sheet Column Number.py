'''
先遍历这个字符串 然后每次result需要乘26
然后再加上字母的值 
'''


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in s:
            result *= 26
            result += ord(i) - ord("A") + 1
        return result