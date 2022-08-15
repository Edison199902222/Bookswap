class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)
        left = 0
        for right in range(len(s)):
            if s[right] == " ":
                self.reverse(s, left, right - 1)
                left = right + 1
            elif right == len(s) - 1:
                self.reverse(s, left, right)
        return s

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
'''
先逆转整个string
然后对于每个string 一个一个逆转
'''