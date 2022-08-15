'''
用了stack
把stack中储存前缀 和之前的数字
如果遇到【就进入栈
如果遇到】就输出
'''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curnum = 0
        curstring = ""
        for char in s:
            if char =="[":
                stack.append(curstring)
                stack.append(curnum)
                curstring = ""
                curnum = 0
            elif char =="]":
                prenum = stack.pop()
                prestr = stack.pop()
                curstring = prestr + curstring*prenum
            elif char.isdigit():
                curnum = curnum*10 + int(char)
            else:
                curstring+=char
        return curstring

'''
递归版本
四种情况
1）是数字，就累加之前有的数字
2）是左括号，从左括号之后开始递归。递归要传回两个值：组成的substring，递归结束的位置。 之后把传回的substring × 数字 加到结果里。数字归零。
3）是右括号，返回结果
4）是普通字母，直接加到结果里
感觉这种思路比较简洁好懂一些

'''


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.dfs(0, s)

    def dfs(self, index, s):
        string = ""
        digit = 0
        # index 记录当前index 遍历到哪
        i = index
        while i < len(s):
            # 如果遇到左括号
            if s[i] == "[":
                # 直接把里面的string 整理 return，并且return 右括号的index
                temp, j = self.dfs(i + 1, s)
                # 把里面的string 乘当前digit 放进当前string 中
                string += digit * temp
                # 变为0
                digit = 0
                i = j + 1
            elif s[i].isdigit():
                # 获取数字
                digit = digit * 10 + int(s[i])
                i += 1
            # 如果遇到右括号，直接return
            elif s[i] == "]":
                return string, i

            else:
                string += s[i]
                i += 1
        return string


if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString("100[leetcode]"))