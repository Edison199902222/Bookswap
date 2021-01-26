class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in num:
            while stack and k and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        while k > 0:
            stack.pop()
            k -= 1
        result = "".join(stack).lstrip("0")
        return result if result else "0"
'''
我们如果要删除数的话，那么肯定我们希望移除  越大越好的数
所以 我们用stack 保持一个单调递增的趋势
如果发现左边的任何一个数 大于右边的数， 我们就把它移除
结束后 如果所有左边的数字都小于等于右边的数组
如果发现 还需要移除数字
那么我们就把右边的数 移除 因为右边的数组是大于左边的
'''