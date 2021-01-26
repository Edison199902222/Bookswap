'''
1）首先，对一个字符串来说，要去除首位的空格符。

（2）字符e，只能出现数字后面，且e后面不能出现小数点(.)，也就是e后面必须是整数。

（3）+ 、-号，只能出现在首位，或者紧跟e的后面，其他情况均不对。

（4）小数点(.)只能出现一次，且只能是出现在e的前面。

（5）根据上面几条规则，可以设置几个标识符，例如，isDot, isDigit, isE 扫描一边字符串，即可完成。

'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        is_dot,is_digit,is_E = False,False,False
        if len(s) < 0:
            return False
        for i, x in enumerate(s):
            if x == "e":
                if not is_digit or is_E: # 前面没有数字，or 前面已经存在字符 e
                    return False
                is_digit = False #设置isDigit = false
                is_E = True
            elif x in "+-":
                if i != 0 and s[i-1]!="e": # +- 只能出现首位，和 字符e的后面
                    return False
            elif x == ".":
                if is_dot or is_E: # 字符 .（小数点）只能出现一次，而且是只能出现在 e 的前面
                    return False
                is_dot = True
            elif x.isdecimal():  # 检查字符串是否只包含十进制字符
                is_digit = True
            else:
                return False
        if is_digit:  # 最后要检查 是否含有数字
            return True
        else:
            return False
if __name__ =="__main__":
    solution = Solution()
    print(solution.isNumber("-1."))
