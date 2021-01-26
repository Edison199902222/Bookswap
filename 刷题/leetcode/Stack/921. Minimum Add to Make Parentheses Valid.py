class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        # 记录需要右括号 的数量
        left = 0
        result = 0
        for i in range(len(S)):
            # 如果遇到左括号，说明需要一个右括号，left + 1
            if S[i] == "(":
                left += 1
            else:
                # 遇到右括号，如果需要右括号的数量大于0，则可以 - 1 抵消
                if left > 0:
                    left -= 1
                # 不然的话，那么我们多出一个右括号，需要添加左括号
                else:
                    result += 1

        return result + left

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0
        # 记录左 右括号数量
        left = 0
        right = 0
        result = 0
        for i in range(len(S)):
            # 遇到左括号，直接 left + 1
            if S[i] == "(":
                left += 1
            # 遇到右边括号
            else:
                # right 先加 1
                right += 1
                # 如果发现右边括号数量比左边括号多， 那么result 就需要添加左括号，添加左括号的数量是 right left 的差
                # 清空left  right
                if right > left:
                    result += right - left
                    right = 0
                    left = 0
        # 最后还要检查 left 是否大于 right
        if left > right:
            result += left - right
        return result