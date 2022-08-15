class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = list(S)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            else:
                if not s[left].isalpha():
                    left += 1
                if not s[right].isalpha():
                    right -= 1
        return "".join(s)
'''
isalpha 是用来判断 一个字符串是不是全是由字母组成
用双指针的办法 如果两个都是字母就交换位置
不然的话 就移动
'''