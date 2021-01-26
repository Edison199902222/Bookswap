'''
建立一个stack
维持一个单调递减的stack
遍历T 如果发现 现在的元素 大于stack的顶部元素的话
那么我们就知道 一个warm day来了
那么我们就更新result result其实就会等于 warm day 的index 相减
并且把stack 顶部元素pop出去
stack 中储存的是index
'''



class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        result = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result