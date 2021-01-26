'''
用stack 储存的是为匹配的左括号的索引 也代表合法括号串起始的位置
初始化stack 放进一个 -1 来保证起始位置
遇到 左括号就放进stack中
如果遇到 右括号 那么我们就pop 一个左括号出来， 代表进行匹配
如果pop 出左括号以后 stack变成空的，说明合法括号串没有起始位置了，之前有不合法的括号 使不能继续下去，需要重新把当前index 放进stack中 作为起始位置
如果没有空，那么我们就更新result 用当前index 减去 stack 栈顶元素

'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 初始化，记录左括号的位置
        stack = [-1]
        result = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                # 通过 当前右边括号 跟 stack中是否 还有有左括号来判断当前右括号是否合法
                stack.pop()
                # 如果没有左括号了，是不合法，重新记录第一个不合法的位置，因为初始化，不需要担心stack 为空
                if not stack:
                    stack.append(i)
                # 有左括号的话 通过当前i 减去 左括号的位置，这个区间就是当前合法的位置
                else:
                    result = max(result, i - stack[-1])
        return result

if __name__ =="__main__":
    solution = Solution()
    print(solution.longestValidParentheses("(()"))