'''
想法 使用stack 并且使用字典
先在字典里 把右括号和左括号相匹配
然后遍历字符串 1 如果是左括号 每次压入stack
2 不是左括号 就跟stack顶元素相比
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_dic = {')' : '(','}' : '{', ']' : '['}
        for i in s:
            if i not in s_dic:
                stack.append(i)
            elif not stack or s_dic[i] != stack.pop():
                return False
        return not stack # 最后要判断stack是否是空 如果是空的话才可以 有东西就是不合法的
