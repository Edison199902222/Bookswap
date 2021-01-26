class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 需要右括号的个数
        balance = 0
        min_step = 0
        for char in s:
            if char == "(":
                balance += 2
                # 遇到左括号，代表上一轮结束，如果上一轮需要有括号的个数为奇数的话，说明有奇数个右括号，没有完全与左边匹配上
                if balance % 2 == 1:
                    balance -= 1
                    # 相当于添加了一个右括号
                    min_step += 1
            else:
                balance -= 1
            # 小于0说明，右边括号数量大于左括号，需要添加左括号
            if balance < 0:
                min_step += 1
                balance += 2
        min_step += balance
        return min_step


class Solution:
    def minInsertions(self, s: str) -> int:
        min_step = 0
        # 记录有多少个左括号需要匹配
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                # 左括号直接入栈
                stack.append(s[i])
            else:
                # 两种情况，一种 如果右括号是最后一个的话
                if i == len(s) - 1:
                    # 两种情况 一种stack中有未匹配的左括号
                    if stack:
                        # 对于单独的一个括号，我们再添加一个右括号就可以跟stack中的左括号匹配
                        min_step += 1
                        stack.pop()
                    else:
                        # 如果没有左括号，只能加一个右括号，加一个左括号
                        min_step += 2
                # 当前遇到的右括号不是最后一个
                else:
                    # 有未匹配的左括号
                    if stack:
                        # 如果stack中有未匹配的右括号，并且下一个还是右括号
                        if s[i + 1] == ")":
                            # 直接匹配，当前的跟下一个右边括号，跟stack最后一个消掉
                            stack.pop()
                            i += 1
                        else:
                            # 下一个不是右括号，那么直接添加一个右边括号
                            min_step += 1
                            stack.pop()
                    # 没有左括号
                    else:
                        # 下一个是右括号的话
                        if s[i + 1] == ")":
                            # 添加一个左括号，来消掉
                            min_step += 1
                            i += 1
                        # 不是右括号的话
                        else:
                            # 添加一个左括号 一个右括号
                            min_step += 2
            i += 1
        return min_step + len(stack) * 2

class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "}")
        open_count = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "(":
                open_count += 1
            else:
                # 加一个右括号，因为所有的 )) 都变成 }
                # 如果单独一个右括号出现，那么说明这个右括号后面没有另一个右括号
                if s[i] == ")":
                    result += 1
                if open_count:
                    open_count -= 1
                # 加一个左括号
                else:
                    result += 1
        return result + open_count * 2

