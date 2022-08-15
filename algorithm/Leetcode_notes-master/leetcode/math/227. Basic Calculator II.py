class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        stack = []
        # 初始化设置为+，目的是我们需要遇到的第一个数字先push进stack中，然后当遇到第一个符号时，更新符号， 遇到第二个符号时，在计算第一个符号
        # 因为stack是记录每一个加减乘除符号之前的结果， 因为这里面有乘除号，所以我们需要用stack储存前面的信息， 不能直接像basic cacualate1 一样直接计算加减号
        sign = "+"
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c in "+-*/":
                if sign in "+-":
                    if sign == "+":
                        stack.append(number)
                    else:
                        stack.append(-number)
                elif sign in "*/":
                    if sign == "*":
                        stack[-1] = stack[-1] * number
                    else:
                        stack[-1] = int(stack[-1] / number)
                number = 0
                sign = c
        if sign in "+-":
            if sign == "+":
                stack.append(number)
            else:
                stack.append(-number)
        else:
            if sign == "*":
                stack[-1] = stack[-1] * number
            else:
                stack[-1] = int(stack[-1] / number)
        return sum(stack)
'''
与224 一样的思路
初始化 sign 为 +
sign 储存的是上一次的加减乘除符号， i 会储存成 现在的加减乘除符号
每一次遇到新的加减乘除符号，我们就计算上一次sign中储存的符号，因为只有这样，才能满足优先级顺序
比如 3 + 2 / 1 我们需要先算2/1， 遇到/ 时， 我们先计算之前两个+号， 把3 跟 2 放进stack中
然后 等循环结束，我们计算 2/1

只不过 我们使用stack储存每一次的结果
最后 把stack中所有结果家在一起就是最终结果
因为 有*/号 所以 我们需要储存前一次的值 
number 是当前的数字
sign是符号
遇到 符号 我们就进行操作
我们就看之前的sign 是什么 如果是+ 号 就直接把数字append进stack中
如果是 - 号 那么我们需要 -num 进入stack
如果是 * 号 那么我们把stack最后一位pop出来 乘以现在的数字 再放进去
/ 号也一样
最后还要把number 清零 
sign 变成 当前字符

循环结束后  还需要添加一次 因为1 + 2 这种  如果循环结束不检查的话
2 就不会添加进去
'''


class Solution:
    def calculate(self, s: str) -> int:
        # 思路： 遇到 加号 减号 直接push 进stack 就可以
        # 用stack 的原因是， 如果遇到 乘 或者 除 需要前面的数字来进行运算
        # stack 记录每一个数字，如果遇到乘或者除 直接跟stack 顶部元素进行合并即可
        # 遇到数字时，如果数字下一个不是数字，说明这一段数字已经截止了， 那么根据之前的sign 来push 进stack
        stack = []
        sign = "+"
        number = 0
        for i in range(len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])
                if i + 1 < len(s) and s[i + 1].isdigit():
                    continue
                if sign == "+":
                    stack.append(number)
                elif sign == "-":
                    stack.append(-number)
                elif sign == "*":
                    stack.append(stack.pop() * number)
                else:
                    stack.append(int(stack.pop() / number))
                number = 0
            elif s[i] in "+-*/":
                sign = s[i]
        return sum(stack)

    class Solution:
        def calculate(self, s: str) -> int:
            stack = []
            number = 0
            sign = "+"
            for i in range(len(s)):
                if s[i].isdigit():
                    number = number * 10 + int(s[i])
                elif s[i] in "+-*/":
                    if sign == "+":
                        stack.append(number)
                    elif sign == "-":
                        stack.append(-number)
                    elif sign == "*":
                        stack.append(int(stack.pop() * number))
                    elif sign == "/":
                        stack.append(int(stack.pop() / number))
                    sign = s[i]
                    number = 0
                if i == len(s) - 1:
                    if sign == "+":
                        stack.append(number)
                    elif sign == "-":
                        stack.append(-number)
                    elif sign == "*":
                        stack.append(stack.pop() * number)
                    elif sign == "/":
                        stack.append(int(stack.pop() / number))
            return sum(stack)




