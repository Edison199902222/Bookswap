'''
这道题很巧妙
用一个遍历 这个遍历比较特殊
是由 第一个字符串的长度 减去第二个字符串的长度 + 1
然后 每次切片第一个字符串 切片的长度就是第二个字符串的长度 然后对比两个一不一样
一样return i

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
