class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        stack.append(["#",0])
        for char in s:
            if char == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char,1])
        string = ""
        for i in range(1, len(stack)):
            string += stack[i][0] * stack[i][1]
        return string
'''
创建stack 
初始化stack 防止stack中是空的 
stack 中 会储存 以字符 跟它出现的次数组成的list
然后遍历 字符串
遇到char 跟stack中最后一个的字符 相同的话，就把它的数量加1
并且检查 如果刚好等于k的话， 就把它移除
如果遇到其他的字符的话， 就把字符添加进stack中
最后再整合再一起
'''