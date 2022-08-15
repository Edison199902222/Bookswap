class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        for i in range(len(arr)):
            if not stack or arr[i] >= stack[-1]:
                stack.append(arr[i])
            elif stack and arr[i] < stack[-1]:
                curmax = stack[-1]
                while stack and arr[i] < stack[-1]:
                    stack.pop()
                stack.append(curmax)
        return len(stack)
'''
什么时候需要新增加一个chunk？
如果我们遇到后面的数组 比前面最大值 大的时候，就证明我们需要新添加一个chunk
如果 后面的数组 一直比前面的最大值小的话，我们只需要一个chunk就行了

所以， 我们建立一个递增的单调栈
如果当前元素比 stack栈顶元素大于或者等于的话 我们就放进去
如果比栈顶元素小的花，那么我们就要考虑合并了chunk了
首先 cur max 等于当前栈顶元素， 因为栈顶元素肯定是最大的 这是递增的stack
然后我们比较 当前元素 跟stack 栈顶， 如果stack 比 栈顶小，那么就把stack pop出来，直到找到一个栈顶元素 小于等于当前元素 这样就表示 不用继续合并了
最后再把curmax 放进stack中

总结下来就是 假设我们很多个chunk， 每个chunk的从左到右的条件是，每一个chunk 的最大值 要小于等于右边的 chunk的最小值
所以 stack中每一个元素都是代表 chunk的最大值
每一次合并chunk时， 合并的元素都可能代表的是当前chunk的最小值， 所以我们要找到第一个小于等于它的 作为分界点
'''