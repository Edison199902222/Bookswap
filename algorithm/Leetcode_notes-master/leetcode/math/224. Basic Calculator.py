class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        current_number = 0
        result = 0
        sign = 1
        for c in s:
            if c in "1234567890":
                current_number = current_number * 10 + int(c)
            elif c == "+":
                result = result + sign * current_number
                current_number = 0
                sign = 1
            elif c == "-":
                result = result + sign * current_number
                current_number = 0
                sign = -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += current_number * sign
                current_number = 0
                pre_sign = stack.pop()
                pre_result = stack.pop()
                result = result * pre_sign + pre_result
        result += sign * current_number
        return result

'''
current_number 表示当前操作的数
sign表示当前操作数应该被加还是被减
result表示最后的结果
遍历字符串

如果遇到数字了 那么我们就把数字加到current 的尾端
如果遇到+号了 说明 前一段的数字需要被计算 放进结果了 所以把result = result + sign * current_number
并且把current number 重新设置为0 sign 设置为1

如果遇到- 号了 同样的 说明前一段数字需要被计算了
把current number设置为0 但是sign需要设置为-1 表示负号
如果遇到左括号了说明我们要优先算右边的表达式 我们就把之前累计的result 跟sign 放进stack中 此时sign表示括号内的结果 需要被result加上还是减去
案后初始化result 跟sign

如果遇到右边括号了 说明一个括号内的表达式被计算完了,先把右括号前面的数字 放进result中 然后把current number设置为0
此时需要从栈中取出该括号之前的sign和result, 与当前的result相加运算 (注意, 是原来的result + sign * 当前result)

以及, 循环结束后number可能还有数字, 需要加到result里. (比如"1+2"这样的表达式, 2并不会在循环内被加到结果中)

'''
if __name__ == "__main__":
    solution = Solution()
    print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))