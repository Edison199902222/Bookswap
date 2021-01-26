class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        remove = set()
        for index, ch in enumerate(s):
            if ch == "(":
                stack.append(index)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(index)
        stack = set(stack)
        result = ""
        for i, ch in enumerate(s):
            if i not in stack and i not in remove:
                result += ch
        return result
'''
首先 创建一个stack 跟 一个remove set
我们遍历字符串
如果发现 左括号就放进stack中 如果发现右边括号 并且stack 中有左括号时 我们就把stack pop出去一个左括号 抵消
如果stack中没有任何东西， 说明 右括号出现在左括号前面 无法抵消 所以放进remobe set 中
最后 stack中剩下的 index 就是无法抵消的左括号
所以 我们把stack 变成set 方便之后 查找
然后我们再次遍历字符串
只要当前元素不在stack跟 remove中 那么就把它放进 result里面去
'''