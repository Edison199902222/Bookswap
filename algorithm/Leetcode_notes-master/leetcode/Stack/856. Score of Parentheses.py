class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type S: str
        :rtype: int
        """

        ans = 0
        d = -1
        for i in range(len(s)):
            if s[i] == "(":
                d += 1
            else:
                d -= 1
            if s[i] == "(" and s[i + 1] == ")":
                ans += 1 << d
        return ans
'''
因为只有（）算成一分
所以每当我们找到一个（）我们只要算它的左边 有几个左括号 我们就✖几个2
比如（（）） 我们找到最里面（） 左边有一个（ 所以是1 乘️ 一个2 

'''

'''
cur 表示每一层的分数
如果我们遇到左括号
我们只需要将这一层的分数先放进stack之中 然后进入下一层 并且更新cur 重新为0
如果遇到右括号 我们就回到上一层 并且把上一层累计的分数 也就stack 的栈顶元素 加上 
如果当前这一层的分数大于等于1的话 那么我们就选择 * 2  或者 如果当前没有分数的话 我们就选择跟前一个左括号形成（）也就是加上一分

'''


class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type S: str
        :rtype: int
        """

        stack = []
        cur = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(cur)
                cur = 0  # 记录当前层的分数，比如（（）（）） 当我们遍历到 里面第二个括号时候， stack top元素是1，
                # 因为前面有一个括号的分数，每当遇到一个左括号 说明要进入下一层或者 进入同一层 另一个括号里面，所有cur 要清零
            else:
                cur = stack.pop() + max(cur * 2, 1)  # 每次遇到右括号，说明我们当前括号已经结束，我们就把前面一层的分数 加上当前层的分数，
                # 当前层分数取决于cur 是不是0，如果不是0 说明连续遇到两个或者多个右括号
        return cur