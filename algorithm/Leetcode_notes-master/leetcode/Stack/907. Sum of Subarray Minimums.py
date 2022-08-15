class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = [0] + A + [0]
        stack = []
        result = 0
        for index, num in enumerate(A):
            while stack and num < A[stack[-1]]:
                temp = stack.pop()
                left_bound = stack[-1]
                result += A[temp] * (index - temp) * (temp - left_bound)
            stack.append(index)
        return result % (10**9 + 7)
'''
先在数组中 前后加0
这样我们可以防止找不到左右边界的问题
我们用stack 去维持一个单调递增的数组
stack的栈顶元素 是当前数字 的左边边界 
我们每次检查 只要当前元素大于stack中的栈顶元素
我们就放进stack中
一旦遇到 小于stack栈顶的元素 
把此时栈顶元素pop出来
我们就知道 当前元素 是pop元素的右边界
那么左边界就是 此时的栈顶元素
我们再用公式 右边界 减去 pop元素index ✖ pop元素index 减去 左边界 这就是以pop元素为最小值得到的连续子数组的组合种类

'''