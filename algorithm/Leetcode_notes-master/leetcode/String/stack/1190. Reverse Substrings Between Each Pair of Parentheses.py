class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [""]
        for c in s:
            if c == "(":
                stack.append("")
            elif c == ")":
                temp = stack.pop()[::-1]
                stack[-1] += temp
            else:
                stack[-1] += c
        return stack.pop()
'''
常规解法 
使用一个stack 初始化设置一个空字符串 目的防止无括号情况 跟 最后大括号的情况
如果遇到左括号 我们就 添加空字符串， 说明 我们要把括号里面的字符放进空字符串里面 来反转
如果没有遇到括号 我们就把遇到的字符加进stack 中的最后一个空字符串中
遇到右括号 把stack中的最后一个（因为最后一个代表里现在右括号最近的一个左括号） 字符拿出来 反转 然后再把它加进stack 中上一个字符中去
'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        temp = []
        dic = {}
        for i, j in enumerate(s):
            if j == "(":
                temp.append(i)
            if j == ")":
                index = temp.pop()
                dic[index] = i
                dic[i] = index
        result = []
        index = 0
        direction = 1
        while index < len(s):
            if s[index] in "()":
                index = dic[index]
                direction = - direction
            else:
                result.append(s[index])
            index += direction
        return ''.join(result)
'''
O（n）的解法
想象一下虫洞
我们创建一个字典
把左括号的index 作为key 右边括号的 index 作为value放进去， 右边括号index 作为key 左边括号作为value 也放进dic中
然后我们创建一个index， direction 指针
如果遇到左括号，我们查找字典，直接跳到右括号的index， 然后direction 取反，本来是从左往右加入字符，现在变成从右往左加入字符
如果没有遇到括号， 把index 指向的字符 直接加入进result中
每次更新idnex
'''