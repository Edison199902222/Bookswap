class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
                continue
            temp = []
            while stack[-1] != "[":
                temp.append(stack.pop())
            stack.pop()
            base = 1
            times = 0
            while stack and stack[-1].isdigit():
                times += int(stack.pop()) * base
                base *= 10
            substring = "".join(reversed(temp))*times
            stack.append(substring)
        return "".join(stack)
'''
用stack 储存之前的信息
如果遇到 右括号
那么说明 我们就从 stack 找到对应的字符串和重复次数，decode 之后再放回 stack 里
最后 再把stack中的所有东西合并
'''