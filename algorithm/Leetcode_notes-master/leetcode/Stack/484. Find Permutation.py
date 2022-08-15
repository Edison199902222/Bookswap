class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if not s:
            return []
        # 储存d 的range
        stack = []
        result = []
        n = len(s)
        # 数组如果全i排列，就是对应的index + 1
        # 其实数组的range是没有变，如果遇到d的话，range 就反转
        for i in range(len(s)):
            if s[i] == "D":
                stack.append(i + 1)
            else:
                # 遇到I，就把之前的反转，因为range 已经储存在stack中了
                stack.append(i + 1)
                while stack:
                    result.append(stack.pop())
        # 最后一个digit要加上
        result.append(n + 1)
        # 如果stack中还有东西，说明一直遇到d， 没有遇到i
        while stack:
            result.append(stack.pop())
        return result

